Weather you are on a linux/macos or a Windows Subsystem for Linux, the scripts should work.
In a terminal session (either direct for linux/macos, or after starting the wsl in CMD), go to your Documents folder and clone :

cd Documents

git clone https://github.com/georgiosdoumas/MirantisScripts.git

cd MirantisScripts

ls -l 

You should see the 3 files. Stay in this folder MirantisScripts and call it.

Usage  for linux (and Windows with wsl) :

./sd_handle.py -c 12345 

where 12345 is the SF case number 

Usage for macos :
python3 sd_handle.py -c 12345

- The script sd_handle.py assumes there is only 1 downloaded docker-support-xxx.zip in your ~/Downloads/ folder. 
And that is why it will move any new zip in another folder, after it finish processing it.

- A new folder named SDextractions will be created under your ~/Documents , and inside SDextractions/ a subfolder named original_sd_zips/.

- The docker-support-xxxx.zip file (after being extracted) will be moved from the Downloads/ in the SDextractions/original_sd_zips/
so if you want to attach them in a Jira case, you will find them there, each under its own subfolder of SF case.

Of course you can use a string that is not only a SF case number, but have something to remind you of what the case is about, for example you can use it as 

./sd_handle.py -c 12345msr (if you want to remind your self that the case was about MSR) or -c 54321upg if it was for a proactive upgrade

In the end  you will get to a structure similar to this :

Documents/SDextractions/

├── 1234567

│   └── docker-support-clustertID1-20210407-14_11_49

│   └── docker-support-clustertID1-20210408-18_13_55

├── 1234568

│   └── docker-support-clusterID2-20210415-10_02_36

├── 1234569

│   └── docker-support-clusterID3-20210415-21_07_52

└── original_sd_zips

|       ├── 1234567
    
|       ├── 1234568
    
|       ├── 1234569
    


At some point (in April I hope) I will transform the sd_patterns_search from bash to py, so somebody with a Windows laptop will not have to bother installing a WSL. So every few days to get the latest versions, do (while you are inside the MirantisScripts/) 

git pull  https://github.com/georgiosdoumas/MirantisScripts.git

