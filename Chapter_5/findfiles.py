import os.path
import datetime
import collections

patth="d://install//"
data  = collections.defaultdict(list)

for root,dirs,files in os.walk(patth):
    dirs[:] = [dir for dir in dirs if not dir.startswith(".")]
    for filename in files:
        fullname = os.path.join(root, filename)
        mod_timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(fullname))
        key = (mod_timestamp, os.path.getsize(fullname))
        data[key].append(fullname)

for size, filename in sorted(data):
    names = data[(size, filename)]
    if len(names)>1:
        print("{0} ({1} bytes) may be duplicated " "({2} files):".format(filename, size, len(names)))
    for name in names:
        print("\t{0}".format(name))

