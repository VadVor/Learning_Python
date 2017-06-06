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

list_files = [name for name in os.listdir(".") if os.path.isfile(name) in {".lst"}]
if len(list_files) == 0:
    filename = get_string("Choose file name: ", "filename")
    if not filename:
        raise CancelledError()
    if not filename.endswith(".lst"):
        filename += ".lst"
    print("\n--No items are in the list--")
    new_file = get_string("[A]dd [Q]uit", "new_file", default="a")
print(list_files)