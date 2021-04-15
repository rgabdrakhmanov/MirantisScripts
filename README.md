MirantisScripts

Weather you are on a linux/macos or a Windows Subsystem for Linux , this script should work.

Go to your Documents folder and clone :

git clone https://github.com/georgiosdoumas/MirantisScripts.git

cd MirantisScripts

ls -l 

You should see the 3 files 

Usage :

./sd_handle.py -c 12345 

where 12345 is the SF case number 

A new folder named SDextractions will be created under your ~/Documents , and inside SDextractions a subfolder named original_sd_zips

The docker-support-xxxx.zip files will be moved in the SDextractions/original_sd_zips/

so if you want to attach them in a Jira case, you will find them there, each under its own subfolder of SF case

So you will get to a structure similar to this :

~/Documents/SDextractions/
                          12345/docker-support-1/extracted-folders-here
                          12345/docker-support-2/extracted-folders-here
                          12346/docker-support-1/extracted-folders-here
                          original_sd_zips/12345/docker-support-1.zip
                          original_sd_zips/12345/docker-support-2.zip
                          original_sd_zips/12346/docker-support-1.zip
