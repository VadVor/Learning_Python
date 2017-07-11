import os.path
import datetime
import argparse


patth="d:/install/"
data = []

parser = argparse.ArgumentParser(description='The paths are optional; if not given . is used.', 
                                 usage='%(prog)s [options] [path1 [path2 [...pathN]]]')
parser.add_argument('-H', '--hidden', required=False, action='store_true', help="show hidden files [default: off]")
parser.add_argument('-m', '--modified', required=False, action='store_true', help="show last modified date/time [default: off]")
parser.add_argument('-o', '--order', default="name", type=str, help="order by ('name'-'n', 'modified'-'m', 'size'-'s') [default: name]")
parser.add_argument('-r', '--recursive', required=False, action='store_true', help="recurse into subdirectories [default: off]")
parser.add_argument('-s', '--sizes', required=False, action='store_true', help="show sizes [default: off]")
parser.add_argument('path', default='d:/install/', action='store_true')
args = parser.parse_args()
for root,dirs,files in os.walk(patth):
    dirs[:] = [directory for directory in dirs if not directory.startswith(".")]
    for filename in files:
        fullname = os.path.join(root, filename)
        mod_timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(fullname))
        data.append((mod_timestamp, os.path.getsize(fullname), fullname))
    break
if args.order in ("modified", "m"):
    data.sort(key=lambda tup: tup[0])
elif args.order in ("size", "s"):
    data.sort(key=lambda tup: tup[1])
else:
    data.sort(key=lambda tup: tup[2])   
for datta in data:
    print("{0:.19}   {1:>10}  {2:<} ".format((lambda:"" if args.modified==False else str(datta[0]))(), 
                                             (lambda:"" if args.sizes==False else datta[1])(), datta[2]))   
for directory in dirs:
    print("                                  "+patth+directory)
print("{0} file{1},".format(len(files),(lambda:"" if len(files)==1 else "s")()), end=" ")
print("{0} director{1}".format(len(dirs),(lambda:"y" if len(dirs)==1 else "ies")()))
print()

parser.print_help()
