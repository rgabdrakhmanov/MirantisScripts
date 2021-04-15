MirantisScripts

Weather you are on a linux/macos or a Windows Subsystem for Linux , this script should work.

In a terminal session (either direct for linux/macos, or after starting the wsl in CMD), go to your Documents folder and clone :

git clone https://github.com/georgiosdoumas/MirantisScripts.git

cd MirantisScripts

ls -l 

You should see the 3 files. Stay in this folder MirantisScripts and call it.

Usage :

./sd_handle.py -c 12345 

where 12345 is the SF case number 

The script sd_handle.py assumes there is only 1 downloaded docker-support-xxx.zip in your ~/Downloads/ folder. And that is why it will move any new zip in another folder.

A new folder named SDextractions will be created under your ~/Documents , and inside SDextractions a subfolder named original_sd_zips

The docker-support-xxxx.zip file (after being extracted) will be moved from the Downloads/ in the SDextractions/original_sd_zips/

so if you want to attach them in a Jira case, you will find them there, each under its own subfolder of SF case.

So you will get to a structure similar to this :

~/Documents/SDextractions/

                          12345/docker-support-1/extracted-folders-here
                          
                               /docker-support-2/other-extracted-folders-here
                          
                          12346/docker-support-1/extracted-folders-here
                          
                          original_sd_zips/12345/docker-support-1.zip
                          
                                                /docker-support-2.zip
                          
                                           12346/docker-support-1.zip
                          
