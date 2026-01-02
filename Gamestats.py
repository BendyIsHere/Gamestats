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

# ------------------------------------- CASUAL FUNCTIONS --------------------------------

def clearr():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")

clearr()

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
    genres = ""
    tags = ""
    stores = ""
    for a,b in enumerate(fgame["stores"]):
        stores += fgame["stores"][a]["store"]["name"] + "\n "
    for a,b in enumerate(fgame["genres"]):
        genres += fgame["genres"][a]["name"] + ", "
    for a,b in enumerate(fgame["tags"]):
        tags += fgame["tags"][a]["name"] + ", "
    print(" | " + str(fgame["name"]).upper() + " | ")
    print("Release Date : " + str(fgame["released"]) + " | Rating : " + str(fgame["rating"])+ " | Ratings count : " + str(fgame["ratings_count"])+"\nGenres : "+genres+" | Metacritic : "+str(fgame["metacritic"])+"\n Sells on: \n"+stores+"\n Tags : "+tags)

def findgamestat(statt,inn):  # find one specific game statistic
    pages = 1
    url = "https://api.rawg.io/api/games"
    params = {
        "page":pages,
        "key":API_KEY,
        "search":inn
    }
    r = requests.get(url,params=params)
    fgame = r.json()["results"][0]
    print(" | " + str(fgame["name"]).upper() + " | ")
    print(statt + ": " + fgame[statt])

def findrandom(inn:int): # Finds A random game from a random page
    clearr()
    rpage = random.randint(1,inn)
    results = searchpage(rpage)
    gamesnumber = 0
    for i,v in enumerate(results):
        if (i % 7) == 0 :
            gamesnumber += 1
    gnumber = random.randint(0,gamesnumber)
    for i,v in enumerate(results):
        if i == gnumber * 7:
            print("Game : "+ v +" | Rating : "+ str(results[i + 1])+" | Ratings : "+ str(results[i + 2]) + "\n | Genres : "+ str(results[i + 3]) + " Release Date : " + str(results[i + 4]) + "\n \nSells on : \n" + str(results[i+5]) + "\n")

# ----------------------- COMMAND INTERFACE ----------------------------------------

print(r"""
  ________   __  ____________________ __________
 / ___/ _ | /  |/  / __/ __/_  __/ _ /_  __/ __/
/ (_ / __ |/ /|_/ / _/_\ \  / / / __ |/ / _\ \  
\___/_/ |_/_/  /_/___/___/ /_/ /_/ |_/_/ /___/  
            made by BendyIsH3re
    -using RAWG API
      """)
testingMode = False



while testingMode == False:
    print(" ")
    innphrase = input("$USER$-|-: ")
    inn = innphrase.split()

    if not inn:
        continue

    if inn[0].lower() == "getstats":
        if len(inn) > 1:
            gamename = ""
            for i,v in enumerate(inn):
                if i > 0:
                    gamename += v + " "
            gamename = gamename[:-1]
            findgame(gamename)
        else: print("[Syntax Error] : provide a game name")

    elif inn[0].lower() == "getstat":
        gamename = ""
        for i,v in enumerate(inn):
            if i > 1:
                gamename += v
                gamename += " "

        gamename = gamename[:-1]
        findgamestat(inn[1],gamename) if len(inn) > 2 else print("[Syntax Error] : [getstat (STATISTIC) (GAME NAME)] - to find all statistics type : help statistics")
    
    elif inn[0].lower() == "random":
        if len(inn) > 2:
            findrandom(inn[1])
        else:
            findrandom(20)

    elif inn[0] == "help":
        if len(inn) < 2:
            print("Commands : getstats [GAME NAME] - getstat [STATISTIC] [GAME NAME] - help [NONE or statistics or debug] - exit")
        elif len(inn) == 2:
            if inn[1].lower() == "statistics":
                print(" STATISTICS : name | ratings | ratings_count or ratingsc | genres | released or release_date or rdate \n stores or sellers | slug")
            elif inn[1].lower() == "debug":
                print(" DEBUG CMDS : DB_allstats | DB_checkapi | DB_rawdata")
    
    elif inn[0] == "clear":
        clearr()
    
    elif inn[0].lower() == "exit":
        clearr()
        testingMode = True
    
    elif inn[0] == "DB_allstats":
        values()
    
    elif inn[0] == "DB_checkapi":
        print(checkapi())
    
    elif inn[0] == "DB_rawdata":
        print(rawdata(inn[1])) if len(inn) > 1 else print("[Syntax error] : DB_rawdata [pagenumber]")
    
    else:
        print("[General Error] : " + inn[0] +" is an invalid command")