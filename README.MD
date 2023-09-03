<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Discord Message Logger and Webhook Sender</title>
</head>

<body>

    <h1>Discord Message Logger and Webhook Sender</h1>

    <p>This Python script is designed to log messages from a Discord channel and send them to a webhook. It can be useful for various applications such as monitoring, archiving, or integrating Discord messages into other platforms.</p>

    <h2>How it works</h2>

    <p>The script accomplishes its task through the following steps:</p>

    <ul>
        <li><code>channel_id</code>: The ID of the Discord channel you want to log messages from.</li>
        <li><code>authorization_token</code>: Your Discord bot's authorization token.</li>
        <li><code>webhook_url</code>: The URL of the webhook where the messages will be sent.</li>
        <li><code>last_checked_time</code>: The script keeps track of the last checked message timestamp, starting with a default value of one hour ago.</li>
        <li><code>processed_messages</code>: A set to store processed message IDs to avoid duplicating messages.</li>
    </ul>

    <ol start="2">
        <li><strong><code>send_to_webhook</code> Function</strong>: This function formats the message data and user information and sends it to the webhook. It does the following:</li>
    </ol>

    <ul>
        <li>Fetches user information using the provided authorization token.</li>
        <li>Constructs a message embed with user data, message content, and optional file links (attachments).</li>
        <li>Sends the message to the webhook.</li>
    </ul>

    <ol start="3">
        <li><strong><code>get_new_messages</code> Function</strong>: This function retrieves new messages from the specified Discord channel. It fetches messages using the provided authorization token and returns the messages in JSON format.</li>
    </ol>

    <ol start="4">
        <li><strong>Main Loop</strong>: The script runs in an infinite loop, periodically checking for new messages in the Discord channel.</li>
    </ol>

    <ul>
        <li>It compares the message timestamps to the last checked time to identify new messages.</li>
        <li>If a new message is found, it processes the message using the <code>send_to_webhook</code> function and updates the last checked time.</li>
    </ul>

    <h2>Getting Started</h2>

    <p>To use this script, follow these steps:</p>

    <ol>
        <li>Clone the repository to your local machine.</li>
    </ol>

    <pre><code>git clone https://github.com/HarakyV/Discord-Message-Logger.git</code></pre>

    <ol start="2">
        <li>Configure the script by providing your <code>channel_id</code>, <code>authorization_token</code>, and <code>webhook_url</code>.</li>
    </ol>

    <ol start="3">
        <li>Run the script using Python (<code>python discord_message_logger.py</code>).</li>
    </ol>

    <p>The script will continuously monitor the specified Discord channel and send new messages to the webhook.</p>

    <h2>Contributing</h2>

    <p>If you want to contribute to this project, feel free to open issues or pull requests. We welcome your contributions!</p>

    <h2>License</h2>

    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>

</html>
