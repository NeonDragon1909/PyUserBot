#!/usr/bin/python3

from telethon import TelegramClient, events, sync
import data

with TelegramClient('userbot', data.api_id, data.api_hash) as client:
	client.start()
    print(client.get_me().stringify())