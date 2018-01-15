def dir_content_paths(sPath):
    import os
    for sChild in sPath:
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            dir_content_paths(sChildPath)
        else:
            print (sChildPath)

if __name__ == ("__main__"):
    dir_content_paths("C:\\Users\\gshkr")
