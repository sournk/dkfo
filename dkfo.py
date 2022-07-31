# dkfo - File Orginizer Script
# Author: Denis Kislitsyn
# Email: denis@kislitsyn.me
#   
# Script gets one param - src_dir path.
# Script moves all files and subdirs older than 2 days from src_dir into !Archive/%dd subdirs.
# Script is useful for Downloads folder. Just add script into your cron task.

import os
import sys
import time
import shutil
import datetime as dt

ARCHIVE_DIR_NAME = '!Archive' # Subdir name is destanation for moving files in
DONT_TOUCH_FILES_DEPTH_DAYS = 2 # Paths with cdate early today()-DONT_TOUCH_FILES_DEPTH_DAYS are skiped

def is_old_file(file):
    '''
    Check creation date of file. If it's created earlier then DONT_TOUCH_FILES_DEPTH_DAYS days file is old.
    '''
    
    old_file_edge = dt.datetime.today() - dt.timedelta(days=DONT_TOUCH_FILES_DEPTH_DAYS)
    old_file_edge = old_file_edge.timestamp()
    return os.path.getmtime(file) < old_file_edge
    
path_src = sys.argv[1]
path_dst = os.path.join(path_src, ARCHIVE_DIR_NAME)

files = [os.path.join(path_src, f) for f in os.listdir(path_src)] # list of full paths files and dirs
files = filter(lambda path: path != path_dst, files) # delete archive dir from list, becasue it's not necessary to move this dir from top level
files = filter(is_old_file, files) # filter earlier paths from list 
files = sorted(files)

for f in files:
    day = time.strftime('%d', time.gmtime(os.path.getctime(f)))
    path_dst_day = os.path.join(path_dst, day)
    os.makedirs(path_dst_day, exist_ok=True)
    try:
        shutil.move(f, os.path.join(path_dst_day, os.path.basename(f)))
        print(f'[INFO] Path archived {f}')
    except Exception as e:
        print(f'[ERROR] Path is not moved: {str(e)}')
