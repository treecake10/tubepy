from pytube import YouTube
#from utils.lang import downloadstatus, url_input
import json

# try to read from config.json file where to store the downloaded video
location:str = ''
def download(youtube_url):
    
    with open('utils/config.json', 'r') as file_location:
        location = json.load(file_location)
        preferred_location = location["download_location"]
        print(preferred_location)
     

# using new_location for testing purposes
new_location:str = "~/Music"
def change_download_location(new_location):
    try:
        with open('utils/config.json', 'r') as file_location:
            default_location = json.load(file_location)

        default_location["download_location"] = new_location

        with open('utils/config.json', 'w') as file_location:
            json.dump(default_location, file_location, indent=4 )
        
    except Exception:
        print(" empty default location")

change_download_location(new_location)
     