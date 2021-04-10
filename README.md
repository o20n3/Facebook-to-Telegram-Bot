# Facebook-to-Telegram-Bot
Telegram bot which scrapes posts from Facebook Pages and sends to a Telegram channel.
This project has been forked from [VariabileAleatoria/Telegram-Facebook-Pages-Bot](https://github.com/VariabileAleatoria/Telegram-Facebook-Pages-Bot)

This is also my very first project in github and I am by no means a professional. 

## Concept

From an online privacy perspective, many people choose to forego social media accounts, yet still need to interact with members of Facebook communities. This bot will monitor and send new posts from public Facebook pages to your Telegram account so that you don't need to deal with visiting those pages without an account and all the crap which that entails. This can also be a handy tool to receive updates in Telegram for your important Facebook pages in the event that you have notifications for Facebook turned off.

## Setting Up Telegram Channel

For this project to work, it must have a Telegram channel, an active bot with admin rights, and an API Token for the bot. Follow these steps to set up your Channel:

1. Create a new Telegram Channel by selecting the hamburger icon (three lines) in the desktop app or the 'create' pencil in the mobile app and then choose 'New Channel'.
2. Give your channel a name you will associate with the Facebook pages you are scraping and an icon (or you can add this later).
3. Using the Telegram search function, search for **BotFather** [sic] or use this link: [BotFather](https://telegram.me/botfather)
4. Type `/newbot` and follow the instructions. **NB: If this is your first bot, I would make the name and username the same thing.**
5. Once you have given your bot a username, BotFather creates it for you and shares the bot's **Token**. This is important for adding to your config file later. If you forget your token, you can always check the post history of BotFather or type `/mybots` into BotFather to see info on your bots.
6. Now you need to give your new bot Admin access to your Telegram Channel. Go back to your new channel and tap the name to go to Channel Info. Inside here you can manage Administrator users. (This is a very different process for Telegram's desktop and mobile platforms so hopefully you can work it out on your own.) Once you find 'Add Administrator', begin searching for the name you gave your bot and then once you see it, add it to your channel.
7. That's it. Your Telegram channel and bot are now ready to recieve scraped data from Facebook. Now to configure the server side

## Setting Up Server

I have been working on the setup.py file to automate the server setup process.

[facebook-scraper](https://github.com/kevinzg/facebook-scraper) only gets the last two or three posts, keep that in mind if your pages posts more than 3 times in two minutes, or just change the check interval accordingly.  

## What's working
Right now the library used only retrieves text posts and photos, so no videos, shares or others

## Python Modules needed

The setup.py file will now install the module dependencies below.

[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)  
[facebook-scraper](https://github.com/kevinzg/facebook-scraper)
