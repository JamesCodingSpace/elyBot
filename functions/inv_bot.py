import webbrowser
import sys
sys.path.append("./settings")
from setting_functions import get_app_id # type: ignore

def open_inv_link():
    id = get_app_id("app_id:")
    try:
        webbrowser.open(f"https://discord.com/oauth2/authorize?client_id={id}&scope=bot&permissions=0")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

