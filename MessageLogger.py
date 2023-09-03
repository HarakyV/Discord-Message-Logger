import requests
import time
from datetime import datetime, timedelta, timezone

channel_id = ''
authorization_token = ""
webhook_url = ''
last_checked_time = datetime.now(timezone.utc) - timedelta(hours=1)
processed_messages = set()


def send_to_webhook(content, user_id, avatar_url, file_links=None):
    headers = {
        'authorization': authorization_token
    }
    response = requests.get(f'https://discord.com/api/v9/users/{user_id}', headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        username = user_data['username']
        roles = user_data.get('roles', [])
        role_names = []
        for role_id in roles:
            role_response = requests.get(f'https://discord.com/api/v9/guilds/{channel_id}/roles/{role_id}',
                                         headers=headers)
            if role_response.status_code == 200:
                role_data = role_response.json()
                role_names.append(role_data['name'])

        embed = {
            'title': f'Message from User ID: {user_id}',
            'description': content,
            'thumbnail': {'url': avatar_url},
            'fields': [
                {'name': 'Username', 'value': username, 'inline': True},
                {'name': 'Roles (dont work)', 'value': ', '.join(role_names) if role_names else 'No Roles', 'inline': True}
            ]
        }

        if file_links:
            for file_link in file_links:
                embed['description'] += f'\n\n[File Link]({file_link})'

        payload = {
            'embeds': [embed]
        }
        webhook_response = requests.post(webhook_url, json=payload)
        if webhook_response.status_code == 204:
            print("Message sent to webhook successfully.")
        else:
            print("Failed to send message to webhook.")
    else:
        print("Failed to fetch user information.")


def get_new_messages():
    headers = {
        'authorization': authorization_token
    }
    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


while True:
    messages = get_new_messages()
    if messages:
        for message in messages:
            message_id = message['id']
            if message_id not in processed_messages:
                message_time = datetime.strptime(message['timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z')
                if message_time > last_checked_time:
                    content = message['content']
                    user_id = message['author']['id']
                    avatar_url = message['author']['avatar']

                    file_links = []
                    attachments = message.get('attachments', [])
                    for attachment in attachments:
                        attachment_url = attachment['url']
                        file_links.append(attachment_url)

                    send_to_webhook(content, user_id, f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_url}.png',
                                    file_links)
                    processed_messages.add(message_id)
                    last_checked_time = message_time
    else:
        print("Failed to fetch messages.")
