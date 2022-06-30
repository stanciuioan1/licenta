import shutil
import os
 
# path to source directory
src_dir = '1'
 
# path to destination directory
dest_dir = '2'
 
# getting all the files in the source directory
files = os.listdir(src_dir)

for i in range(3,481):
    dest_dir = str(i)
    shutil.copytree(src_dir, dest_dir)