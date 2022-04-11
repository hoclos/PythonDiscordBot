# Python Discord Bot

### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

```terminal.sh-session
git clone https://github.com/hoclos/PythonDiscordBot.git
cd PythonDiscordBot
heroku container:login
heroku create
heroku config:set DISCORD_TOKEN="<discord token here>"
```
Configure Dyno on your [Heroku Dashboard](https://dashboard.heroku.com/apps)
