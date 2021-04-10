#!/usr/bin/env python3

import telegram, threading
from facebook_scraper import get_posts
from datetime import datetime
import csv
from tempfile import NamedTemporaryFile
import shutil
import bot_conf

TOKEN = bot_conf.TOKEN
bot = telegram.Bot(TOKEN)

chat_id = bot_conf.chat_id

date_format = '%Y-%m-%d %H:%M:%S'

fields = ['telegram_name', 'fbpage_tag', 'last_post_date']

WAIT_SECONDS = 120

def check():
    with open('fbpages.csv', mode='r+') as csv_file, NamedTemporaryFile(mode='w', delete=False) as tempfile:
        csv_reader = csv.DictReader(csv_file)
        csv_writer = csv.DictWriter(tempfile, fields)
        line_count = 0
        csv_writer.writeheader()
        for page in csv_reader:
            temp = None
            posts = list(get_posts(page['fbpage_tag'], pages=2))
            posts.sort(key = lambda x: x['time'])
            for post in posts:
                if post['time'] <= datetime.strptime(page['last_post_date'], date_format): # post already sent to channel
                    break
                if post['image'] is not None:
                    bot.send_photo(chat_id, post['image'], (post['text'] if post['text'] else '')+ '\n[' + page['telegram_name'] + ']')
                    if (post['time'] > datetime.strptime(page['last_post_date'], date_format) and temp is None):
                        temp = post['time']
                elif post['text'] is not None:
                    bot.send_message(chat_id, (post['text'] if post['text'] else '')+ '\n[' + page['telegram_name'] + ']')
                    if (post['time'] > datetime.strptime(page['last_post_date'], date_format) and temp is None):
                        temp = post['time']
            if temp is not None:
                page['last_post_date'] = temp
            row = {'telegram_name': page['telegram_name'], 'fbpage_tag': page['fbpage_tag'], 'last_post_date': page['last_post_date']}
            csv_writer.writerow(row)
        shutil.move(tempfile.name, 'fbpages.csv')
        threading.Timer(WAIT_SECONDS, check).start()

check()
