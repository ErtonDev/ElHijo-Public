<p align="center">
  <img src="https://raw.githubusercontent.com/ErtonDev/ElHijo-Public/main/resources/logo.png" width="100"/>
  <h1 align="center">El Hijo (Public)</h1>
</p>

[![Python 3.8](https://img.shields.io/badge/python-3.9-yellow.svg)](https://www.python.org/)
[![Build](https://img.shields.io/badge/Supported_OS-Linux-orange.svg)]()
[![GitHub Repo stars](https://img.shields.io/github/stars/ErtonDev/ElHijo-Public?style=social)](https://github.com/ErtonDev/ElHijo-Public)
[![GitHub forks](https://img.shields.io/github/forks/ErtonDev/ElHijo-Public?style=social)](https://github.com/ErtonDev/ElHijo-Public)

**ElHijo-Public** contains the scripts for my multifunctional discord bot *El Hijo* (Code is mostly in spanish, but I'll try to explain everything here as best as I can). I designed *El Hijo* for my friend's discord server as a fun way to add some administration and entertainment elements to the server. The project that once started as a short 100 lines script that answered you if you typed 'Hi' slowly became a 2000 lines beast with functions like:

1. Administration tools for specific server roles
2. Personal *El Hijo* accounts to save bot-person related data
3. An investing simulator with fictional stocks to win bot's credits (stored in your account)
4. A casino with games to spend bot's credits
5. And lots of other commands to enhance the bot's overall capabilities

<p align="center">
  <img src="https://raw.githubusercontent.com/ErtonDev/ElHijo-Public/main/resources/example.png"/>
</p>

Sadly, the bot doesn't work anymore due to discord.py library not being supported and the latest discord API changes which, basically, break the traditional system most discord.py bots were using. Despite the bad news, I thought I could upload it here to show how it used to work as someone may find it useful.

<p align="center">
  <img src="https://raw.githubusercontent.com/ErtonDev/ElHijo-Public/main/resources/elhijo.png" height = 300/>
</p>

---
## Getting Started 🚀

El Hijo V7.8.2 was the last update I made. The last patch included all of the following files:

1. bot.py (Main file)
2. logclass.py (A class with console logging methods)
3. mercado.py (Script running in the background to control the investing simulator prices)
4. niveles.py (Series of useful functions to edit and check specific values of a personal account)
5. database.py (Tool to navigate through my extremely embarrassing txt files based database)

> Everything that had to do with the bot's resources or the database wasn't uploaded to the repository

---
## Dependencies 📁

El Hijo used the following modules:
 - discord https://pypi.org/project/discord.py/
 - subprocess *(Default python)*
 - itertools *(Default python)*
 - colorama https://pypi.org/project/colorama/
 - random *(Default python)*
 - time *(Default python)*
 - math *(Default python)*
 - os *(Default python)*
 - io *(Default python)*
 - re *(Default python)*
 
 ---
## Execution 💻

<p align="left">
  <img src="https://logodownload.org/wp-content/uploads/2022/05/linux-logo.png" height=100/>
</p>

#### For Linux, Ubuntu...
Execute the following command in your terminal inside the **ElHijo-Public** folder:

```
python3 bot.py
```
> You may also use *python2* or simply *python* depending on your version

<p align="center">
  <img src="https://raw.githubusercontent.com/ErtonDev/ElHijo-Public/main/resources/execution.png" height=500/>
</p>

Once the bot was on, members of the server could type commands after the prefix '.' such as '.auxilio', which sent a discord embed with a detailed list of all the bot's commands. Other commands like '.admin' or '.mod' granted access to moderation tools for administrators of the server, and those who weren't could use '.perfil' or '.ficha' to check their personal accounts. These accounts stored data such as points, credits or even information about their misdeeds! Administrators could send warnings to these accounts when someone was doing something that they shouldn't. And lastly, the commands '.banco' and '.casino' allowed you to play different games, where you spent the credits won by investing in the simulator to win prizes!

<p align="center">
  <img src="https://raw.githubusercontent.com/ErtonDev/ElHijo-Public/main/resources/elhijo_commandnotfound2.png" height=200/>
</p>

I'm sure I won't be uploading the bot anymore as it would mean to redo most of the code, but at least I will have it here as a piece of educational content for anyone trying to learn python.
