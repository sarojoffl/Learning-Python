import requests
import hashlib
import time
import os
from plyer import notification

# URL of the page to monitor
url = 'https://www.wikidata.org/wiki/Wikidata:Administrators%27_noticeboard'
# Path to the file where the page hash will be stored
hash_file_path = 'page_hash.txt'

def get_page_hash(url):
    """
    Fetches the page content from the URL and returns its MD5 hash.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the request failed
    content = response.text
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def send_notification():
    """
    Sends a desktop notification indicating that the page has been updated.
    """
    notification.notify(
        title='Page Updated!',
        message='The page has changed. Check it out!',
        timeout=10  # Duration in seconds for which the notification is displayed
    )

def main():
    """
    Main function to monitor the page for updates.
    """
    first_run = True
    
    # Check if the hash file already exists
    if os.path.exists(hash_file_path):
        # Read the previous hash from the file
        with open(hash_file_path, 'r') as file:
            previous_hash = file.read().strip()
        first_run = False
    else:
        # If the hash file does not exist, initialize it with the current page hash
        previous_hash = ''
        current_hash = get_page_hash(url)
        with open(hash_file_path, 'w') as file:
            file.write(current_hash)
    
    # Continuously check the page for updates
    while True:
        current_hash = get_page_hash(url)
        
        # If it's not the first run and the hash has changed, send a notification
        if not first_run and current_hash != previous_hash:
            send_notification()
            # Update the hash file with the new hash
            with open(hash_file_path, 'w') as file:
                file.write(current_hash)
            previous_hash = current_hash
        
        first_run = False
        # Wait for 10 seconds before checking again
        time.sleep(10)

if __name__ == '__main__':
    main()

