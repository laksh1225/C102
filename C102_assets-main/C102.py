import os
import shutil

from_dir = "F:/C102_assets-main/C102_assets-main"
to_dir = "F:/C102_assets-main/C102_assets-main"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)
    if ext == '':
        continue
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir+'/'+file_name
        path2 = to_dir+'/'+'C102'
        path3 = to_dir+'/'+'C102'+'/'+file_name

        if os.path.exists(path2):
            shutil.move(path1, path3)
            print(file_name+"is moving")
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)
            print(file_name+"is moving")
