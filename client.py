#ToDo Rename lol

import os

def GetUsername():
    username = ""
    usernamePath = "C:\Program Files (x86)\Steam\config\loginusers.vdf"
    usernameFile = open(usernamePath)
    for i in usernameFile:
        if "PersonaName" in i:
            username = i.split()[1].strip("\"")
    return username

def findGames(libs):
    xpath = "\\common\\"
    games = []
    for i in libs:
        for j in os.listdir(i + xpath):
            for k in os.listdir(i + xpath + j):
                if ".exe" in k:
                    if j not in games:
                        games.append(j)
                    break
    return games

def findLibs(driveList):
    libraryPaths = ["C:\Program Files (x86)\Steam\steamapps"]
    resp = "n"
    print("Drives Located:")
    for i in driveList:
        print(i)
    print("Checking Steam default install in C: by default")
    if len(driveList) != 1:
        print("would you like to scan other drives?")
        resp = input("y/n? ")
    print()
    if resp == "y":
        for i in driveList[1:]:
            print("Library on " + i)
            print("Please locate steamapps folder path.")
            print("It will be in the form of 'C:\Program Files (x86)\Steam\steamapps'")
            driveLib = input("Please paste drive path here without apostrophe: ")
            print()
            libraryPaths.append(driveLib)
    return libraryPaths

def main():
    username = GetUsername()
    libs = []
    print("Identifying User")
    print("User Found: ")
    print(username)
    print()
    drives = os.popen("fsutil fsinfo drives").readlines()
    driveList = drives[1].split()[1:]
    libs = findLibs(driveList)
    games = findGames(libs)
    print("Games have been successfully detected!!!!\n")
    print(username + " has currently installed:")
    for i in games:
        print(i)
    
    

main()
