# Description
A python script that can be used to check if a web store has available stock for a certain product.
It simply retrieves the page content every couple minutes and looks for a specific text string that indicates NO stock. If the string is NOT found, a notification is pushed to a device using pushbullet.

# Usage
Create an `.env` file in the root directory to add and store the configuration.

  ```sh
  # Environment Variables
  URL='STORE URL HERE'  # Replace with store page URL
  SEARCH_TEXT='TEXT CONDITION HERE'  # Replace with the text that indicates NO STOCK on the store page
  PUSHBULLET_TOKEN='TOKEN HERE'  # Replace with your actual Pushbullet API token
  PUSHBULLET_URL='https://api.pushbullet.com/v2/pushes'  # PushBullet API
  CHECK_INTERVAL=1800  # 30 minutes
  ```

Then simply run `run_script.bat` to execute the script.
