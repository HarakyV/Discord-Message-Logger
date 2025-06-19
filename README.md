# Discord Message Logger and Webhook Sender
This is a discord self bot logger
This Python script is designed to log messages from a Discord channel and send them to a webhook. It can be useful for various applications such as monitoring, archiving, or integrating Discord messages into other platforms.

## How it works

The script accomplishes its task through the following steps:

- `channel_id`: The ID of the Discord channel you want to log messages from.
- `authorization_token`: Your Discord bot's authorization token.
- `webhook_url`: The URL of the webhook where the messages will be sent.
- `last_checked_time`: The script keeps track of the last checked message timestamp, starting with a default value of one hour ago.
- `processed_messages`: A set to store processed message IDs to avoid duplicating messages.

2. **`send_to_webhook` Function**:  
   This function formats the message data and user information and sends it to the webhook. It does the following:
   - Fetches user information using the provided authorization token.
   - Constructs a message embed with user data, message content, and optional file links (attachments).
   - Sends the message to the webhook.

3. **`get_new_messages` Function**:  
   This function retrieves new messages from the specified Discord channel. It fetches messages using the provided authorization token and returns the messages in JSON format.

4. **Main Loop**:  
   The script runs in an infinite loop, periodically checking for new messages in the Discord channel.
   - It compares the message timestamps to the last checked time to identify new messages.
   - If a new message is found, it processes the message using the `send_to_webhook` function and updates the last checked time.

## Getting Started

To use this script, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/HarakyV/Discord-Message-Logger.git
