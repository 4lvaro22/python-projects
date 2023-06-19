import os

def gettingPath():
    print("Actual path: " + os.getcwd())
    path = input("Enter the path where you want to remove the folders: ")
    return path

def removeFolders(path):
    try:
        for i in range(1, 10):
            os.removedirs(path + "Folder-" + str(i))
    except OSError as oserror:
        print("Error Message: " + oserror)
    else:  
        print("Folders removed successfully")


if __name__ == "__main__":
    path = gettingPath()
    removeFolders(path)

