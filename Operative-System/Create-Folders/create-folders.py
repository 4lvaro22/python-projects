import os

def gettingPath():
    print("Actual path: " + os.getcwd())
    path = input("Enter the path where you want to create the folders: ")
    return path

def createFolders(path):
    try:
        for i in range(1, 10):
            os.mkdir(path + "Folder-" + str(i))
    except OSError as oserror:
        print("Error Message: " + oserror)
    else:  
        print("Folders created successfully")


if __name__ == "__main__":
    path = gettingPath()
    createFolders(path)

