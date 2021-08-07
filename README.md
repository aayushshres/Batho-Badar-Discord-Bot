# Monke-Discord-Bot
A Discord bot to bring joy in your server.

# Table of contents
* [Setup & Run](#setup-&-run)
* [Hosting for free in Cloud](#hosting-for-free-in-cloud)
* [Developer Notes](#developer-notes)
* [License](#License)

# Setup & Run
* First you need to register a new application or bot at https://discord.com/developers/applications.
* Next, open the `.env` file and specify the token value. Value provided in the file is just for example.
* Add the bot to your discord server and run `main_version-1-0-3.py` file. 
* At this moment this bot runs locally so feel free to add and remove bot features by editing `main_version-1-0-3.py` file and testing it.

# Hosting for free in Cloud
* First go to https://replit.com/ and create a free account.
* Create a new repl for python.
* Create `main.py` and `keep_alive.py` in your new repl.
* Copy and paste the code from the respective `main_version-1-0-3.py` and `keep_alive.py` files from your local machine.
* Create a secret environment variable.
* Uncomment the following lines from `main_version-1-0-3.py`
```
 from keep_alive import keep_alive
 keep_alive()
 my_secret = os.environ['TOKEN']
```
* Run `main.py` and wait for repl to download required modules and run it.(This process might take some time depending on your internet speed)
* You will be able to see the following window:
![alt text](https://github.com/aayushshres/Batho-Badar-Discord-Bot/blob/main/Images%20for%20Readme/link_window.png?raw=true)
* Copy the URL.
* Then, go to https://uptimerobot.com/
* Add a new monitor
* Select monitor type as HTTP(s)
* Add Friendly Name
* Paste the URL.
* Finally create the monitor.
* After you are done creating the monitor your bot will be hosted for free from the cloud.
* Go to your server and enjoy using the bot.
```
```
Visit this [URL](https://youtu.be/SPTfmiYiuok) to learn how to code a discord bot in python and host it for free in cloud.


# Developer Notes
This bot requires python version `3.6+`. Run `monke manual` in chat to explore all the features.

# License
This is a passion project made in the process of learning to code a discord bot and isn't licensed under anything. Feel free to use or modify this project.
