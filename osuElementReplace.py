import os
import shutil

skin_file = input("File to add/replace: ")
osu_dir = input("osu! skins folder directory: ")
print()
response = input("Proceeding on will REPLACE or ADD {} in every skin. Continue? Y/N ".format(skin_file))
print()

if response == "Y" or response == "y":
    osu_skin_list = next(os.walk(osu_dir))[1]
    
    print("Entering {}...".format(osu_dir))
    print()
    
    def scanfolder():
        for folder in osu_skin_list:
            # print os.path.join(osu_dir, folder)
            shutil.copy(skin_file, os.path.join(osu_dir, folder))
            print("{} added to {}!".format(skin_file, folder))
    
    scanfolder()
    
    print()
    print("{} added or replaced in all skins!".format(skin_file))
    print()
else:
    print("Quitting program")