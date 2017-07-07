import os.path
import datetime
import collections

patth="d://install//"
# data  = collections.defaultdict(list)
data = []
list_for_print = []

for root,dirs,files in os.walk(patth):
    dirs[:] = [dir for dir in dirs if not dir.startswith(".")]
    for filename in files:
        fullname = os.path.join(root, filename)
        mod_timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(fullname))
        data.append((mod_timestamp, os.path.getsize(fullname), fullname))
    break
data.sort(key=lambda tup: tup[1])
for datta in data:
    list_for_print.append("{0:.19}    {1:>}     {2:<} ".format(str(datta[0]), str(datta[1]).strip(), str(datta[2]).strip()))
for t in list_for_print:
    print(t)   

