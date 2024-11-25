import requests
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

URL = os.getenv('URL')
SEARCH_TEXT = os.getenv('SEARCH_TEXT')
PUSHBULLET_TOKEN = os.getenv('PUSHBULLET_TOKEN')
PUSHBULLET_URL = os.getenv('PUSHBULLET_URL', 'https://api.pushbullet.com/v2/pushes')
CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', '1800'))

def check_stock():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        content = response.text

        if SEARCH_TEXT not in content:
            print("STOCK AVAILABLE!")
            send_push_notification()
        else:
            print("No stock...")
    except Exception as e:
        print(f"Error checking stock: {e}")

def send_push_notification():
    headers = {
        'Access-Token': PUSHBULLET_TOKEN,
        'Content-Type': 'application/json'
    }
    data = {
        'type': 'link',
        'title': 'STOCK AVAILABLE',
        'body': 'Click the link to view the product.',
        'url': URL
    }
    try:
        response = requests.post(PUSHBULLET_URL, json=data, headers=headers)
        response.raise_for_status()
        print("Push notification sent.")
    except Exception as e:
        print(f"Error sending push notification: {e}")

def main():
    while True:
        check_stock()
        # Sleep for the specified interval
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()