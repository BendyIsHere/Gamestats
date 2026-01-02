# GAMESTATS

an experimental project aimed to get & use game statistics from the RAWG API.

The project itself is meant to be used along with other projects, kind of as a module, but it can still be extremely useful by itself
It can mainly :
  GETSTATS [GAMENAME]- Get all of a game's statistics
  RANDOM [number] - Show you a random game (the higher the number, the higher the amount of results) 
  GETSTAT [STAT] [GAMENAME]

It could be used for :

    - Trying random games
    
    - Finding where you can buy them
    
    - View if a game is as good as people say it is
    
    - Find similar games based on what you like
    
    - Implementing it in a project of yours.

-------------------------------------------

  SETUP :
  
To actually make it work, you must get a rawg api key, which isn't hard to do : https://rawg.io/apidocs

After you're done, copy the key, and use it in this command :
## Windows
```
setx RAWG_API_KEY "[YOUR KEY HERE]" /M
```
## Linux
 - works on most systems
```
sudo bash
```
```
echo 'RAWG_API_KEY="[YOUR KEY HERE]"' /etc/environment
exit
```
