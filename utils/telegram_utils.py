import aiohttp
import asyncio
import os
import json
import logging
import requests
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
BASE_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}'

async def send_message(chat_id, text, reply_markup=None, reply_to_message_id=None):
    # Ensure this function is called within an async context
    # where tasks can be gathered if needed
    try:
        url = f'{BASE_URL}/sendMessage'
        payload = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'Markdown'
        }
        if reply_to_message_id:
            payload['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            payload['reply_markup'] = json.dumps(reply_markup)
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                response.raise_for_status()
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        raise e

def get_telegram_file_url(file_id):
    try:
        url = f'{BASE_URL}/getFile'
        response = requests.get(url, params={'file_id': file_id})
        response_json = response.json()
        if response.status_code != 200 or not response_json.get('ok'):
            logger.error(f"Error getting file URL: {response_json}")
            raise Exception(f"Failed to get file URL: {response_json.get('description', 'Unknown error')}")
        file_path = response_json['result']['file_path']
        return f'https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{file_path}'
    except Exception as e:
        logger.error(f"Error getting file URL: {e}")
        raise e
