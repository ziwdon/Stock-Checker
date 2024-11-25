import requests
import time

# Constants
URL = 'STORE URL HERE' # Replace with store page URL
SEARCH_TEXT = 'TEXT CONDITION HERE' # Replace with the text that indicates NO STOCK on the store page
PUSHBULLET_TOKEN = 'TOKEN HERE'  # Replace with your actual Pushbullet API token
PUSHBULLET_URL = 'https://api.pushbullet.com/v2/pushes' # PushBullet API
CHECK_INTERVAL = 1800 # 30 minutes

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
        # Sleep for CHECK_INTERVAL minutes
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()
