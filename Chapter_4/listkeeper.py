import os


class CancelledError(Exception):
    pass


def get_string(message, name="string", default=None, minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{0} must have at least {1} and at most {2} characters".format(name, minimum_length,
                                                                                                maximum_length))
            return line
        except ValueError as err:
            print("ERROR", err)

def add_new_file_name():
    filename = get_string("Choose file name: ", "filename")
    if not filename:
        raise CancelledError()
    if not filename.endswith(".lst"):
        filename += ".lst"
    print("\n--No items are in the list--")
    return filename                    

def read_record_file(add_new_file_name):
    new_file = get_string("[A]dd [Q]uit", "new_file", default="a")
    list_items= []
    action_items= None
    while True:
        if new_file in {"a", "A"} or action_items in {"a", "A"} :
            add_string=get_string("Add item ", "add_string")
            list_items.append(add_string)
            for l, item in enumerate(list_items,start=1):
                print("{0}. {1}".format(l,item))
            action_items=get_string("[A]dd [D]elete [S]ave [Q]uit ", "add_string", default="a")
            return True
        elif action_items in {"d", "D"}:
            del_string=get_string("Delete item number (or 0 to cancel)", "del_string")
            
        
    return True
    
list_files = [name for name in os.listdir(".") if name.endswith(".lst")]
if len(list_files) == 0:
    add_new_file_name()
else:
    for n,file in enumerate(list_files,start=1):
        print("{0}. {1}".format(n,file))
    number_file = get_integer("Choose number or '"'0'"' for add new file ", "number_file")
if number_file==0:
    add_new_file_name()
    read_record_file(add_new_file_name)
