from enum import Enum 
import requests

class NotifyMethod(Enum): 
    CONSOLE = "console"
    DISCORD = "discord"
    WHATSAPP = "whatsapp"
    GOOGLE_CALENDAR = "google_calendar"

def notify(changes, method):

    if method == NotifyMethod.CONSOLE:
        for change in changes:
            print(f"{assignment_name}'s {field} changed from {old_value} to {new_value}")

    elif method == NotifyMethod.DISCORD:
        # TODO: Add Discord functionality
        
    elif method == NotifyMethod.WHATSAPP:
        #TODO: Add Whatsapp functionality

    elif method == NotifyMethod.GOOGLE_CALENDAR:
    

    else:
        print(f"Invalid method {method} given")
        return
