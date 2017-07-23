import os.path
import datetime
import argparse
import win32api, win32con
import locale


def folder_is_hidden(directory):
    p=path+"\\"+directory
    if os.name== 'nt':
        attribute = win32api.GetFileAttributes(p)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    else:
        return p.startswith('.') #linux-osx

locale.setlocale(locale.LC_ALL, "eng") #установка локали для отображения разрядов в цифрах

parser = argparse.ArgumentParser(description='The paths are optional; if not given current dir is used.', 
                                 usage='%(prog)s [options] [path1 [path2 [...pathN]]]')
parser.add_argument('-H', '--hidden', required=False, action='store_true', help="show hidden files [default: off]")
parser.add_argument('-m', '--modified', required=False, action='store_true',
                    help="show last modified date/time [default: off]")
parser.add_argument('-o', '--order', default="name", type=str,
                    help="order by ('name'-'n', 'modified'-'m', 'size'-'s') [default: name]")
parser.add_argument('-r', '--recursive', required=False, action='store_true',
                    help="recurse into subdirectories [default: off]")
parser.add_argument('-s', '--sizes', required=False, action='store_true', help="show sizes [default: off]")
parser.add_argument('path',default=os.getcwd(), nargs='*')
args = parser.parse_args()
if isinstance(args.path, str) is True: # преобразования каталога в элемент списка
    args.path = args.path.split()
for path in args.path:
    dirs = []
    files = []
    root = []
    data = []
    count_files = 0
    for root, dirs, files in os.walk(path):
        if args.recursive is False: #обход только текущего каталога
            dirs[:] = [directory for directory in dirs if not folder_is_hidden(directory)] # анализ скрытого атрибута каталога
            for filename in files:
                fullname = os.path.join(root, filename)
                attribute = win32api.GetFileAttributes(fullname)
                mod_timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(fullname))
                if attribute==32 and args.hidden is False: #анализ атрибута скрытого файла
                    data.append((mod_timestamp, os.path.getsize(fullname), fullname))
                    count_files+= 1
                elif args.hidden is True:
                    data.append((mod_timestamp, os.path.getsize(fullname), fullname))
                    count_files+= 1
            break
        else: #рекурсивный обход каталогов
            for filename in files:
                fullname = os.path.join(root, filename)
                attribute = win32api.GetFileAttributes(fullname)
                mod_timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(fullname))
                if attribute==32 and args.hidden is False:
                    data.append((mod_timestamp, os.path.getsize(fullname), fullname))
                    count_files+= 1
                elif args.hidden is True:
                    data.append((mod_timestamp, os.path.getsize(fullname), fullname))
                    count_files+= 1
    if args.order in ("modified", "m"): #сортировка списка файлов по одному из ключей
        data.sort(key=lambda tup: tup[0])
    elif args.order in ("size", "s"):
        data.sort(key=lambda tup: tup[1])
    else:
        data.sort(key=lambda tup: tup[2])   
    for datta in data:
        if args.sizes is False:
            print("{0:.19}   {1:>12}  {2:<} ".format((lambda: "" if args.modified is False else str(datta[0]))(),
                                             (lambda: "" if args.sizes is False else datta[1])(), datta[2]))
        else:
            print("{0:.19}   {1:>12n}  {2:<} ".format((lambda: "" if args.modified is False else str(datta[0]))(),
                                             (lambda: "" if args.sizes is False else datta[1])(), datta[2]))
    for directory in dirs:
        print("                                  "+path+directory)
    print("{0} file{1},".format(count_files, (lambda: "" if count_files == 1 else "s")()), end=" ")
    if args.recursive is False:
        print("{0} director{1}".format(len(dirs), (lambda: "y" if len(dirs) == 1 else  "ies")()))
    print()

# parser.print_help()
