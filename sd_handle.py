#!/usr/bin/env python3
# sd_handle.py: Utility to handle the downloaded support dump zip
# Will extract it in a folder ~/Documents/SDextractions/sf_case_number and also run the sd_nodes3os.py and the sd_patterns_search.sh
# Prerquisites: files sd_nodes3os.py and sd_patterns_search.sh exist in same folder under Documents folder
# git clone https://github.com/georgiosdoumas/MirantisScripts.git
# cd MirantisScripts
# you should see the 3 files as sd_handle.py, sd_nodes3os.py and sd_patterns_search.sh is executable
# Usage: be in the folder that the 3 files are, and call it as
#        ./sd_handle.py -c 12345  (where 12345 is the SF case number)
# All 3 files developed by George Doumas, send comments to gdoumas@mirantis.com (or find me in slack channel)
import os
import shutil
import zipfile
import argparse
import sys
import glob
import subprocess
import platform
from pathlib import Path

HOSTENV = platform.platform()
if HOSTENV.startswith('Windows'):      ## for a windows laptop, this would be eg 'Windows-10-10.0.19041-SP0'
    WIN, WSL = True, False
elif HOSTENV.find('Microsoft') != -1:  ## for a wsl this can be 'Linux-4.4.0-19041-Microsoft-x86_64-with-glibc2.29'
    WIN, WSL = False, True
else:
    WIN, WSL = False, False            ##  then we are on a linux or macos
SCRIPTSDIR = os.getcwd()
if 'sd_nodes3os.py' in os.listdir():
    import sd_nodes3os
else:
    sys.exit('sd_nodes3os.py is not in the {}, please copy-paste it.'.format(SCRIPTSDIR))
if 'sd_patterns_search.sh' not in os.listdir():
    sys.exit('sd_patterns_search.sh is not in the {}, please copy-paste it.'.format(SCRIPTSDIR))
elif not os.access('sd_patterns_search.sh', os.X_OK):
    sys.exit('sd_patterns_search.sh is not executable, please give it the execute permission.')

HOME = os.path.expanduser("~")
TARGETPATH = os.path.join(HOME, 'Documents', 'SDextractions')
Path(TARGETPATH).mkdir(parents = True, exist_ok = True)    # creates the folders '~/Documents/SDextractions' if they do not exist
if WSL:
    BASEUSERDIR = os.path.abspath(os.getcwd()).split('Documents')[0]   ## that should be /mnt/Users/user name/
    SD_DOWNLOAD_DIR =  os.path.join(BASEUSERDIR, 'Downloads')
else:
    SD_DOWNLOAD_DIR = os.path.join(HOME, 'Downloads')
#sys.exit(" Will search in {}".format(SD_DOWNLOAD_DIR))  ### <-------------

sd_arg_parser = argparse.ArgumentParser(description = "Support Dump handler for downloaded sd zip files", add_help=True)
sd_arg_parser.add_argument('-c', '--case', dest='sfcase', help="The SF case number typed as imple integer: -c 43215", default='0', type=str)
sf_case_arg = sd_arg_parser.parse_args()
sf_case = sf_case_arg.sfcase
if sf_case == '0':
    sys.exit("give the SF case number, as in : \n sd_handle.py -c 12345 ")

downloaded_sd_files = glob.glob(SD_DOWNLOAD_DIR + os.sep + 'docker-support-*zip')
number_of_downloaded_sd = len(downloaded_sd_files)
if number_of_downloaded_sd != 1:
    print("There are {} docker-support-*zip files in {} ".format(number_of_downloaded_sd, SD_DOWNLOAD_DIR))
    print("  Or I am looking in the wrong folder (if I run inside a wsl under Windows)")
    sys.exit("But there should be only 1. Please fix this and try again. Keep only 1 dowloaded docker-support-...zip file.")

sd_name = os.path.basename(downloaded_sd_files[0])
corrected_sd_name = sd_name.replace(' ', '_')  # docker-support-clusterid-YYYY-hh mm ss.zip --> docker-support-clusterid-YYYY-hh_mm_ss.zip
fullpath_sd_zip_no_spaces = os.path.join(SD_DOWNLOAD_DIR, corrected_sd_name)
os.rename(os.path.join(SD_DOWNLOAD_DIR, downloaded_sd_files[0]), fullpath_sd_zip_no_spaces) # do the actual rename of downloaded zip file
target_subfolder_for_extracted = os.path.basename(fullpath_sd_zip_no_spaces.split(sep='.zip')[0]) # create a string without the extension .zip
target = os.path.join(TARGETPATH, sf_case, target_subfolder_for_extracted )
print("------  Will exctract the zip into folder {} ".format(target))

with zipfile.ZipFile(fullpath_sd_zip_no_spaces, 'r') as zipobject:
    zipobject.extractall(path=target)

folder_to_move_sdzip_files = os.path.join(TARGETPATH, 'original_sd_zips', sf_case)
Path(folder_to_move_sdzip_files).mkdir(parents = True, exist_ok = True)
print("------  Will move the downloaded zip under {}".format(folder_to_move_sdzip_files))
shutil.move(fullpath_sd_zip_no_spaces, os.path.join(folder_to_move_sdzip_files, corrected_sd_name))
print("    Doing the nodes summary, and pattern search:")
os.chdir(target)
try:
    sd_nodes3os.getnodes('ucp-nodes.txt')
except :
    print("Could not process nodes with sd_nodes3os.py")
if  WIN:
    sys.exit("Running on a Windows machine, so I cannot call the sd_patterns_search.sh")
else:
    run_sd_patterns = subprocess.run( os.path.join(SCRIPTSDIR,'sd_patterns_search.sh') ) ## sd_patterns_search will be turned into python someday
