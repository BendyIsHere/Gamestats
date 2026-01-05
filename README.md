# GAMESTATS

**GAMESTATS** is an experimental Python project that retrieves and uses video game statistics from the **RAWG API**.

It can be used as a **module** in other projects, or **standalone** via the console.

---

## ✨ Features

-  Retrieve detailed statistics for any game  
-  Display a random game  
-  Show user ratings and Metacritic scores  
-  List genres, tags, and release dates  
-  Find stores where a game can be purchased  
-  Discover similar games  

---

## Project Structure

| File | Purpose |
|-----|------|
| [`gstats.py`](./gstats.py) | Core module for importing into other projects |
| [`gstats_console.py`](./gstats_console.py) | Interactive console for testing and exploration |

---

## ⚙️ Setup

To actually make it work, you must first install all python requirements. A simple command will do it (execute it in the repository folder) :
```
pip install -r requirements.txt
```

Then get a rawg api key from https://rawg.io/apidocs

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
Afterwards you're done with the setup!!

# USAGE

> ⚠️ **Note:**  
> These examples are for the `gstats.py` module.  
> For console commands, run `gstats_console.py` and type `help`.

---

## ⚙ Functions

### `findgamestats(gamename)`  

Retrieve detailed statistics for a specific game. Returns a **dictionary** with multiple keys.

####  Examples:

```python
from gstats import findgamestats

stats = findgamestats("Cyberpunk 2077")

# Access individual statistics
print(stats["name"])     # Game name
print(stats["rating"])   # Average rating
print(stats["ratings"])  # Number of ratings
print(stats["genres"])   # List of genres
print(stats["released"]) # Release date
print(stats["stores"])   # Available stores
print(stats["tags"])     # Game tags
print(stats["metacritic"]) # Metacritic score
---
```
## findrandom [pages] 
 the higher the number the more random the result will get. Works exactly like findgamestats but with a randomized game selection

--------------
# ALL OF THE STATISTICS YOU CAN RETRIEVE :
       [string] "name" - game name
       [string] "rating" - game rating
       [string] "ratings" - amount of ratings
       [list]   "genres" - list of game genres
       [string] "released" - game release date
       [list]   "stores" - where you can buy the game
       [list]   "tags" - game tags
       [string] "metacritic" - game score (weighted average)

