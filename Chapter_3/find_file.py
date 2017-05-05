import os
import sys
import fnmatch
import win32com.client


obj.Filter = ["Computer"]
for comp in object:
    print (comp.Name)

'''for comp in object:
    with open('d:\ccccccc.txt', "a") as file:
        file.write(comp.Name+"\n")
file.close()'''

''' exclude = ['$Recycle.Bin','d:\$RECYCLE.BIN','Windows'] 
for root in ['c:\\', 'd:\\']:
    for folder, subdirs, files in os.walk(root, topdown=True):
        subdirs[:] = [d for d in subdirs if d not in exclude]
        for pattern in ['*.arj', '*.exe', '*.iso', '*.rar', '*.zip', '*.msi', '*.7z', '*.com', '*.mp1', '*.mp2', '*.mp3', '*.mp4', '*.mpg', '*.avi' , '*.mpeg', '*.mkv', '*.flv', '*.wma', '*.mov', '*.asf', '*.7zip']:
            for filename in fnmatch.filter(files, pattern): 
                fullname = os.path.join(folder, filename)
                with open('d:\qqqqqqqq.txt', "a") as file:
                    file.write(fullname+"\n")
                    http://hairetdin.blogspot.com.by/2017/02/python-active-directory.html
                    http://torofimofu.blogspot.com.by/2013/11/ldap-python.html
file.close() '''
        
    
