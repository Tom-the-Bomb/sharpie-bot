# Sharpie Bot

## Cloning The Repository

1. Fork or clone the repository
2. Open a command line utility and `cd` to the root directory of the repository
3. Run `pip install -r requirements.txt` to install the needed dependencies

## Running The Bot
1. Log into the Discord website and navigate to the [applications page](https://discord.com/developers/applications)
2. Click `New Application`
3. Give your application a name
4. Navigate to the `Bot` tab and click `Add Bot`. You will have to confirm by clicking `Yes, do it!`
5. Click the `Copy` button underneath token. **(Do not share this)**
6. Inside the bot directory rename the file called `.env.example` to `.env` and paste the token in the `TOKEN` variable

## Inviting The Bot To A Test Server
1. Create a Discord server where you can test your bot
2. On the [applications page](https://discord.com/developers/applications), select your application and navigate to the `OAuth2` tab.
3. Then select the `URL Generator Tab`
4. Select `bot` **and** `applications.commands` under the `scopes` section. Then tick Administrator under the Bot Permissions section
5. Click the Copy button and paste it into your browser of choice and invite it to your test server.

## Adding Your Code To The Main Project
Once you have a new command or feature working in the bot, you can add it to the main project by creating a new pull request to merge it into the master branch.