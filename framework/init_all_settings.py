import keyring
from main import bot

def init_all_settings(config):
    bot.log.info('Reading config file...')
    with open('data/config.cfg','r') as file:
        for line in file:
            if not line.startswith("#") and "=" in line:
                key_value = line.split('=',1)
                key       = key_value[0].strip()
                value     = key_value[1].strip()

                match key.split('_',1)[0].strip():
                    case 'c':
                        cred = keyring.get_credential(value,None)
                        if cred is not None:    
                            config[key.split("_",1)[-1]+'_username'] = cred.username
                            config[key.split("_",1)[-1]+'_password'] = cred.password
                        else:
                            errMsg = (f"Couldn't find any Generic Windows Credentials with the name: '{value}'. Please make sure this credential name was created under Windows Credentials > Generic Credentials.")
                            bot.log.error(errMsg)
                            raise Exception(errMsg)
                    case _:
                        config[key] = value
    bot.log.info(f'Config object created with {len(config)} items.')