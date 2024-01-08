# pyref
Uipath's ReFramework, but in python. Implements RPA Challenge as demo and quick start.
> _**NOTE:** At the moment, implemented only for Windows (linux/macos tbd)_

## Table of Contents
- [Getting started](#getting-started)
    - [Quick start - Windows](#quick-start-guide---windows-1011)
    - [Non-quick start - Windows](#non-quick-start-guide---windows-1011)
- [About](#about)

## Getting started 
### Quick start guide - Windows 10/11
1. Download [install.bat](install.bat) script, and run it as admin. It will:
- install python 3.11, if not installed already 
- download this repo locally (downloads to ``%USERPROFILE%``)
- create and restore virtual environment for the project

2. Run ``cmd.exe``, paste this command to run the project:
```cmd
cd %USERPROFILE%\pyref-1.0.6 && .\venv\Scripts\activate.bat && python main.py
```
### Non-quick start guide - Windows 10/11
1. Make sure you have python installed 
2. Clone the repo locally
3. Open local repo folder in ``cmd.exe``
4. Create a python virtual environment called ``venv``
```cmd
python -m venv venv
```
5. Activate the created virtual environment
```cmd
.\venv\Scripts\activate.bat
```
6. Restore dependencies
```cmd
pip install -r requirements.txt
```
7. Run the project
```cmd
python main.py
```
## About
TBD
