from flows import *
from setup import logger
from helium import click, write, press

def process(t_item,browser):
    
    logger.log.info(f"Process started...")
    
    # Fill in the form (update with the actual field labels/names)
    write(t_item['First Name'], into='First Name')
    write(t_item['Last Name '], into='Last Name')
    write(t_item['Company Name'], into='Company Name')
    write(t_item['Role in Company'], into='Role in Company')
    write(t_item['Address'], into='Address')
    write(t_item['Email'], into='Email')
    write(str(t_item['Phone Number']), into='Phone Number')

    # Assuming there is a 'Submit' button after filling the form
    click('Submit')