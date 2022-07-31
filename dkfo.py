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
import argparse

def is_old_file(file, file_age_limit):
    '''
    Check creation date of file. If it's created earlier than file_age_limit days file is old.
    '''
    
    old_file_edge = dt.datetime.today() - dt.timedelta(days=file_age_limit)
    old_file_edge = old_file_edge.timestamp()
    return os.path.getmtime(file) < old_file_edge
    
parser = argparse.ArgumentParser(description='dkfo script orginize directory by moving files from dir/!Archive/dd')
parser.add_argument("--dir", default='.', type=str, help="Path to orginize. Default is '.'")
parser.add_argument("--file_age_limit", default=0, type=int, help="Moves only files older than age limit in days. Default is 0 days.")
parser.add_argument("--subdir_name", default='!Archive', type=str, help="Name of subdir to move files in. Default is '!Archive'")
args = parser.parse_args()

path_src = args.dir
path_dst = os.path.join(path_src, args.subdir_name)

files = [os.path.join(path_src, f) for f in os.listdir(path_src)] # list of full paths files and dirs
files = filter(lambda path: path != path_dst, files) # delete archive dir from list, becasue it's not necessary to move this dir from top level
files = filter(lambda f: is_old_file(f, args.file_age_limit), files) # filter earlier paths from list 
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
