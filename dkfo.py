# dkfo - File Orginizer Script
# Author: Denis Kislitsyn
# Email: denis@kislitsyn.me
#   
# Script gets one param - src dir path.
# Script moves all files and subdirs from src dir into !Archive/%dd subdirs.
# Script is useful for Downloads folder. Just add script into your cron task.

import os
import sys
import time
import shutil

# Subdir name is destanation for moving files in
ARCHIVE_DIR_NAME = '!Archive'

path_src = sys.argv[1]
path_dst = os.path.join(path_src, ARCHIVE_DIR_NAME)

files = sorted(filter(lambda path: path != path_dst, [os.path.join(path_src, f) for f in os.listdir(path_src)]))
for f in files:
    day = time.strftime('%d', time.gmtime(os.path.getctime(f)))
    path_dst_day = os.path.join(path_dst, day)
    os.makedirs(path_dst_day, exist_ok=True)
    try:
        shutil.move(f, os.path.join(path_dst_day, os.path.basename(f)))
        print(f'[INFO] Path archived {f}')
    except Exception as e:
        print(f'[ERROR] Path is not moved: {str(e)}')
