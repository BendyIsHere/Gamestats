# GAMESTATS

an experimental project aimed to get & use game statistics from the RAWG API.

The project itself is meant to be used along with other projects, kind of as a module, but it can still be extremely useful by itself
It can mainly :

 - Get all of a game's statistics
   
 - Show you a random game (the higher the number, the higher the amount of results)

------------------------------------------

[gstats.py](/gstats.py) is meant to be used onto your projects

[gstats_console.py](/gstats_console.py) instead is used for user interface, for testing & using the different commands avaiable.

The console can be used for :

    - Trying random games
    
    - Finding where you can buy them
    
    - View if a game is as good as people say it is
    
    - Find similar games based on what you like
    
    - Testing and finding all the different functions you could use in your project

-------------------------------------------

  SETUP : 

To actually make it work, you must first install all python requirements. A simple command will do it (execute it in the repository folder) :
```
pip install requirements.txt
```

then get a rawg api key from https://rawg.io/apidocs

After you're done, copy the key, and use it in this command :
## Windows
```
setx RAWG_API_KEY "[YOUR KEY HERE]" /M
```
## Linux
 - works on most systems

Enter as root :
```
sudo bash
```
Set the environment variable  :
```
echo 'RAWG_API_KEY="[YOUR KEY HERE]"' /etc/environment
exit
```
Afterwards just

