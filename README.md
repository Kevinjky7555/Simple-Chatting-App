<h1 align="center">Welcome to Simple Chatting App 👋</h1>

```
   _____ _                 __        ________          __  __  _            
  / ___/(_)___ ___  ____  / /__     / ____/ /_  ____ _/ /_/ /_(_)___  ____ _
  \__ \/ / __ `__ \/ __ \/ / _ \   / /   / __ \/ __ `/ __/ __/ / __ \/ __ `/
 ___/ / / / / / / / /_/ / /  __/  / /___/ / / / /_/ / /_/ /_/ / / / / /_/ / 
/____/_/_/ /_/ /_/ .___/_/\___/   \____/_/ /_/\__,_/\__/\__/_/_/ /_/\__, /  
                /_/                                                /____/
```

Open source python based app for fun to chat with your friends (or yourself)

![Screenshot](https://media.discordapp.net/attachments/861707176064974868/1182027029244284988/image.png)

## What's working?
- Setting your own username
- Join any channel upon opening the app
- Send messages to other people in the same channel as you

![Screenshot](https://cdn.discordapp.com/attachments/861707176064974868/1182032860778090676/image.png)

## Requirements:
- Python 3.7 or higher
- colorama

## Running the server
In a terminal, type __`pip install -r requirements.txt`__ then __`python Server.py`__

![Screenshot](https://cdn.discordapp.com/attachments/861707176064974868/1182032559580917871/image.png)

## Configuring host
If you want to host the server, you will need to configure the ip and port of both server and app.

- App
```py
def checkAddress(self, type=None):
        if (type != None):
            if (type == 0):
                if (self.var['v3'] == "127.0.0.1"): # IP the app should connect to
                    if (self.var['v5'] == 5001): # Port
                        return True
```

Change the ip and port for all of them that appear starting from line 230.

- Server
```py
v2 = 5001;
```

Change the port for the server at line 13.

## Authors

👤 **Kevin** (main developer)

* Github: [@Kevinjky7555](https://github.com/Kevinjky7555)
* Discord: kevinjky7555

Special thanks to:
* lwitchy

## Need help?
Add me on discord: kevinjky7555

# Show your support
Give a ⭐️ if you think this is cool 😼
