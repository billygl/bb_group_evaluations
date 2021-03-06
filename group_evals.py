import sys
import os
import re
import pathlib

arguments = len(sys.argv) - 1
folderpath = ""
if arguments == 1:
    folderpath = sys.argv[1]
else:
    print("usar: group_evals.py %FOLDER_PATH%")
    sys.exit()

# move files in folders
for root, subdirs, files in os.walk(folderpath):
    if root != folderpath:
        break
    for filename in files:
        filepath = os.path.join(root, filename)
        m = re.search('\_(\d{8})', filename)
        identifier = filename
        if m:
            identifier = m.group(1)
        #print(identifier)
        folder = os.path.join(root, identifier)
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.rename(filepath, os.path.join(folder, filename))

#rename folders, files
renaming_folders = []
for root, subdirs, files in os.walk(folderpath):
    student = None
    f = 0
    for filename in files:
        f = f + 1
        filepath = os.path.join(root, filename)
        m = re.search('(\_\d{8}\_intento\_[\d\-]{19})(.*)(\.txt)?', filename)
        if m:
            suffix = m.group(2)
            if suffix == '.txt':
                with open (filepath, 'rt', encoding="utf8") as file:
                    line = file.readline()
                    mn = re.search('Nombre: ([\w ]*)', line)
                    if mn:
                        student = mn.group(1).lower()
                new_name = str(f) + '_intento.txt'
            else:
                new_name = str(f) + suffix
            os.rename(filepath, os.path.join(root, new_name))
    if student is not None:
        SEPARATOR = ' '
        if student not in root:
            os.rename(root, root + SEPARATOR + student)