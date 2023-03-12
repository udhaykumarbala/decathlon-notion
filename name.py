import os
# print all directory names
for folder in os.listdir():
    if os.path.isdir(os.path.join(folder)):
        print(folder)