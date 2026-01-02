import requests
import os
import random
import platform

#VARIABLES & LISTS

API_KEY = os.getenv("RAWG_API_KEY")

statnums = {
    "name":0,
    "rating":1,
    "ratings_count":2,
    "ratingsc":2,
    "genres":3,
    "released":4,
    "release_date":4,
    "rdate":4,
    "stores":5,
    "sellers":5,
    "slug":6,
} 

# ------------------------------------- USAGE --------------------------------------

# Functions :

# findgamestats [gamename] - use it to obtain a dictionary of different statistics of a chosen game

#  EXAMPLES:
# print(findgamestats["name"])
# print(findgamestats["rating"])

# -------------------------------

# findrandom [pages] - the higher the number the more random the result will get. Works like findgamestats but random

#  EXAMPLES:
# print(findrandom["name"])

# --------------
# ALL STATISTICS YOU CAN RETRIEVE :
#        "name"
#        "rating"
#        "ratings"
#        "genres"
#        "released"
#        "stores"
#        "tags"
#        "metacritic"


# ------------------------------------- CASUAL FUNCTIONS --------------------------------

def clearr():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")

if not API_KEY:
    raise RuntimeError(" [RAWG_API_KEY] ENVIROMENT VARIABLE IS NOT SAVED IN THE SYSTEM!!!")

def values():  # Print out all the types of game data
    params = {
        "key" : API_KEY,
        "page" : 1
    }
    url = "https://api.rawg.io/api/games"
    r = requests.get(url,params=params)
    data = r.json()
    print(data["results"][0].keys())

def Search(phrase : str,inn : str) -> bool: #searches for matches in 2 phrases (sensibility changes it's result)
    Sensibility = 2
    phrase1 = phrase.lower()
    inn = inn.lower()
    finalword = ""
    leng = len(inn)
    score = 0
    maxscore = 0
    for i,v in enumerate(phrase1):
        if score < leng:
            if v == inn[score]:
                finalword += inn[score]
                score += 1
                if maxscore < score:
                    maxscore = score
            else:
                finalword = ""
                score = 0

    if not finalword == "" and maxscore > Sensibility:
        return True
    else: return False

def checkapi():
    url = "https://api.rawg.io/api/games"
    params = {
        "key" : API_KEY,
        "page" : 1
    }
    r = requests.get(url,params=params)
    return(r.status_code)

def rawdata(pagee):
    url = "https://api.rawg.io/api/games"
    params = {
        "key" : API_KEY,
        "page" : pagee
    }
    r = requests.get(url,params=params)
    data = r.json()
    return(str(data))

# -------------------------------- RAW API DATA RETRIEVAL -------------------------------------------

def searchfor(pagess): #
    page = 1
    listt = []
    url = "https://api.rawg.io/api/games"
    for i in range(pagess):
        params = {
            "key" : API_KEY,
            "page" : page
        }
        print(API_KEY)
        r = requests.get(url,params=params)
        data = r.json()
        for i,v in enumerate(data["results"]):
            listt.append(v["name"])
            listt.append(v["rating"])
            listt.append(v["ratings_count"])
            genres = ""
            stores = ""
            for a,b in enumerate(data["results"][i]["genres"]):
                genres += data["results"][i]["genres"][a]["name"] + ", "
            for a,b in enumerate(data["results"][i]["stores"]):
                stores += data["results"][i]["stores"][a]["store"]["name"] + "\n "
            listt.append(genres)
            listt.append(v["released"])
            listt.append(stores)
            listt.append(v["slug"])
        page += 1
    return listt

def searchpage(page): #searches all of the games in only one specific page
    listt = []
    url = "https://api.rawg.io/api/games"
    params = {
        "key" : API_KEY,
        "page" : page
    }
    r = requests.get(url,params=params)
    data = r.json()
    for i,v in enumerate(data["results"]):
        fgame = data["results"][i]
        stores = []
        genres = []
        tags = []
        for a,b in enumerate(fgame["stores"]):
            stores.append(fgame["stores"][a]["store"]["name"])
        for a,b in enumerate(fgame["genres"]):
            genres.append(fgame["genres"][a]["name"])
        for a,b in enumerate(fgame["tags"]):
            tags.append(fgame["tags"][a]["name"])
        dictt = {
            "name":str(fgame["name"]),
            "rating":str(fgame["rating"]),
            "ratings":str(fgame["ratings_count"]),
            "genres":genres,
            "released":str(fgame["released"]),
            "stores":stores,
            "tags":tags,
            "metacritic":str(fgame["metacritic"])
        }
        listt.append(dictt)
        page += 1
    return listt

def searchgame(gamename,page): #searches all of the games in only one specific page
    listt = []
    url = "https://api.rawg.io/api/games"
    params = {
        "key" : API_KEY,
        "page" : 1,
        "search" : gamename
    }
    r = requests.get(url,params=params)
    data = r.json()
    for i,v in enumerate(data["results"]):
        listt.append(v["name"])
        listt.append(v["rating"])
        listt.append(v["ratings_count"])
        genres = ""
        stores = ""
        for a,b in enumerate(data["results"][i]["genres"]):
            genres += data["results"][i]["genres"][a]["name"] + ", "
        for a,b in enumerate(data["results"][i]["stores"]):
            stores += data["results"][i]["stores"][a]["store"]["name"] + "\n "
        listt.append(genres)
        listt.append(v["released"])
        listt.append(stores)
        listt.append(v["slug"])
    return listt


# ---------------------- GAME LOOKUP FUNCTIONS  (Data Filtering) -------------------------------


def findgame(inn): # find a game and print out all it's statistics
    pages = 1
    url = "https://api.rawg.io/api/games"
    params = {
        "page":pages,
        "key":API_KEY,
        "search":inn
    }
    r = requests.get(url,params=params)
    fgame = r.json()["results"][0]
    genres = []
    tags = []
    stores = []
    for a,b in enumerate(fgame["stores"]):
        stores += fgame["stores"][a]["store"]["name"]
    for a,b in enumerate(fgame["genres"]):
        genres += fgame["genres"][a]["name"]
    for a,b in enumerate(fgame["tags"]):
        tags += fgame["tags"][a]["name"]
    dictt = {
        "name":str(fgame["name"]),
        "rating":str(fgame["rating"]),
        "ratings":str(fgame["ratings_count"]),
        "genres":genres,
        "released":str(fgame["released"]),
        "stores":stores,
        "tags":tags,
        "metacritic":str(fgame["metacritic"])
    }
    return dictt

def findrandom(inn:int): # Finds A random game from a random page
    clearr()
    rpage = random.randint(1,inn)
    results = searchpage(rpage)
    gamesnumber = len(results)
    gnumber = random.randint(0,gamesnumber - 1)
    print(gnumber)
    print(rpage)
    fgame = results[gnumber]
    dictt = {
        "name":str(fgame["name"]),
        "rating":str(fgame["rating"]),
        "ratings":str(fgame["ratings"]),
        "genres":fgame["genres"],
        "released":str(fgame["released"]),
        "stores":fgame["stores"],
        "tags":fgame["tags"],
        "metacritic":str(fgame["metacritic"])
    }
    return dictt

# --------------------------------------------------------------------------