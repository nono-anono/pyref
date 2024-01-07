@echo off

SETLOCAL ENABLEDELAYEDEXPANSION
    SET "DOWNLOADS_FOLDER=!USERPROFILE!\Downloads"
	SET "PYTHON=!LOCALAPPDATA!\Programs\Python\Python311\python.exe"
    SET "PYTHON_INSTALLER=!DOWNLOADS_FOLDER!\python-3.11.0-amd64.exe"
    SET "PYTHON_URL=https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe"
    SET "FILENAME=python-3.11.0-amd64.exe"

:: Check if Python 3.10 or later is installed
python --version 2>NUL | findstr /R "Python 3\.[1-9][0-9]" >NUL
IF NOT ERRORLEVEL 1 (
	powershell -Command "Write-Host '[INFO] - Python 3.10 or later is already installed' -ForegroundColor Blue"
) ELSE (
	:: Set variables
	powershell -Command "Write-Host '[INFO] - Python 3.10 or later is not installed, downloading installer...' -ForegroundColor Blue"

    FOR /F "tokens=2 delims=-" %%i IN ("!FILENAME!") DO SET "VERSION=%%i"
	
    :: Download Python 3.11 installer
    curl -L "!PYTHON_URL!" -o "!PYTHON_INSTALLER!"
    IF !ERRORLEVEL! NEQ 0 (
		powershell -Command "Write-Host '[ERROR] - Failed to download Python !VERSION!' -ForegroundColor Red"
        GOTO EndScript
    )
	
    :: Run the Python installer
	powershell -Command "Write-Host '[INFO] - Installing Python 3.11.0, please wait...' -ForegroundColor Blue"
    CALL "!PYTHON_INSTALLER!" /quiet InstallAllUsers=0 PrependPath=1 Include_pip=1 Associate_files=1 Include_launcher=1
    IF !ERRORLEVEL! NEQ 0 (
		DEL /F /Q "!PYTHON_INSTALLER!"
		powershell -Command "Write-Host '[ERROR] - Python !VERSION! installation failed due to: !ERRORLEVEL!' -ForegroundColor Red"
        GOTO EndScript
    ) ELSE (
		DEL /F /Q "!PYTHON_INSTALLER!"
		powershell -Command "Write-Host '[INFO] - Python !VERSION! installation was successful' -ForegroundColor Blue"
	)
)

:: Extract the repository name and version tag
SET "REPO_URL=https://github.com/nono-anono/pyref/archive/refs/tags/1.0.6.zip"
for /f "tokens=4 delims=/" %%a in ("!REPO_URL!") do set REPO_NAME=%%a
for /f "tokens=8 delims=/" %%b in ("!REPO_URL!") do set TAG_NAME=%%b
set TAG_NAME=%TAG_NAME:.zip=%
set ZIP_FILENAME=pyref.zip
set ZIP_FILEPATH="%DOWNLOADS_FOLDER%\%ZIP_FILENAME%"
set ZIP_TOPFOLDER=%REPO_NAME%-%TAG_NAME%

powershell -Command "Write-Host '[INFO] - Downloading repo...' -ForegroundColor Blue"
curl -L %REPO_URL% -o "%ZIP_FILEPATH%"
IF %ERRORLEVEL% EQU 0 (
	powershell -Command "Write-Host '[INFO] - Repo download successful, un-archiving repo...' -ForegroundColor Blue"
) ELSE (
    ECHO 
	powershell -Command "Write-Host '[ERROR] - Repo download failed with error code: !ERRORLEVEL!' -ForegroundColor Red"
	GOTO EndScript
)


:: Extracting repo from .zip folder
powershell -Command "Write-Host '[INFO] - Un-archiving repo...' -ForegroundColor Blue"
IF exist "%DOWNLOADS_FOLDER%\%ZIP_TOPFOLDER%" (
	rmdir /s /q "%DOWNLOADS_FOLDER%\%ZIP_TOPFOLDER%"
)
PowerShell -Command "Expand-Archive -LiteralPath '!ZIP_FILEPATH!' -DestinationPath '!DOWNLOADS_FOLDER!'"

:: Move the extracted folder to the destination folder
PowerShell -Command "If (Test-Path -Path '!USERPROFILE!\!ZIP_TOPFOLDER!') { Remove-Item -Path '!USERPROFILE!\!ZIP_TOPFOLDER!' -Recurse -Force }; Move-Item -Path '%DOWNLOADS_FOLDER%\!ZIP_TOPFOLDER!' -Destination '!USERPROFILE!'"

IF %ERRORLEVEL% == 0 (
    DEL /F /Q "%ZIP_FILEPATH%"
	powershell -Command "Write-Host '[INFO] - Repo un-archived successfully and moved to !USERPROFILE!' -ForegroundColor Blue"
) ELSE (
	powershell -Command "Write-Host '[ERROR] - Repo failed to un-archive with error code: !ERRORLEVEL!' -ForegroundColor Red"
	GOTO EndScript
)

CD /d "%USERPROFILE%\%ZIP_TOPFOLDER%"

powershell -Command "Write-Host '[INFO] - Creating virtual environment...' -ForegroundColor Blue"
CALL !PYTHON! -m venv venv

CALL .\venv\Scripts\activate.bat

powershell -Command "Write-Host '[INFO] - Restoring dependencies...' -ForegroundColor Blue"
CALL .\venv\Scripts\pip.exe install -r requirements.txt

powershell -Command "Write-Host '[INFO] - Opening the project folder...' -ForegroundColor Blue"
START .

powershell -Command "Write-Host '[DONE] - Installation and setup completed successfully' -ForegroundColor Green"
:EndScript
PAUSE
EXIT /B 0