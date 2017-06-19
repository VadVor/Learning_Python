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


def get_integer(message, name="integer", default=None, minimum=0, maximum=100, allow_zero=True):

    class RangeError(Exception):
        pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{name} must be between {minimum} and {maximum} inclusive{0}".format(
                    " (or 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))


def add_new_file_name(file_name=None):
    if not file_name:
        file_name = get_string("Choose file name: ", "filename")
        if not file_name:
            raise CancelledError()
        if not file_name.endswith(".lst"):
            file_name += ".lst"
    print("\n--No items are in the list--")
    action = get_string("[A]dd [Q]uit", "new_file", default="a")
    return file_name, action


def read_record_file(file_name, action_items):
    list_items = []
    saved = None
    while True:
        try:
            if action_items in {"a", "A"}:  # добавление элемента
                add_string = get_string("Add item ", "add_string")
                list_items.append(add_string)
                for l, item in enumerate(sorted(list_items, key=str.lower), start=1):
                    print("{0:>{2}}: {1}".format(str(l), item, (lambda: 1 if len(list_items) < 10 else 2
                                                                        if len(list_items) < 100 else 3)()))
                    # print("{0:.2}. {1}".format(str(l), item))
                saved = False
                action_items = get_string("[A]dd [D]elete [S]ave [Q]uit ", "add_string", default="a")
                continue
            elif action_items in {"d", "D"}:  # удаление элимента
                del_string = get_integer("Delete item number (or 0 to cancel)", "del_string")
                if del_string > 0:
                    list_items.pop(del_string-1)
                    for l, item in enumerate(list_items, start=1):
                        if len(list_items) >= 1:
                            print("{0}. {1}".format(l, item))
                    saved = False
                    action_items = get_string("[A]dd [D]elete [S]ave [Q]uit ", "add_string", default="a")
                    continue
                elif del_string == 0:
                    for l, item in enumerate(list_items, start=1):
                        if len(list_items) >= 1:
                            print("{0}. {1}".format(l, item))
                    saved = False
                    action_items = get_string("[A]dd [D]elete [S]ave [Q]uit ", "add_string", default="a")
                    continue
            elif action_items in {"s", "S"}:  # запись элементов
                fh = None
                try:
                    fh = open(file_name, "w", encoding="utf-8")
                    for l, item in enumerate(list_items, start=1):
                        fh.write("{1}\n".format(l, item))
                    print("Saved {0} items to {1}".format(l, file_name))
                    action_items = get_string("Press Enter to continue...", "add_string")
                    print("\n")
                    if action_items is not None:
                        for l, item in enumerate(list_items, start=1):
                            print("{0}. {1}".format(l, item))
                except EnvironmentError as err:
                    print("ERROR", err)
                finally:
                    if fh is not None:
                        fh.close()
                        saved = True
                        action_items = get_string("[A]dd [D]elete [S]ave [Q]uit ", "add_string", default="a")
                continue
            elif action_items in {"o"}:  # чтение записей файла
                try:
                    for line in open(file_name, "r", encoding="utf-8"):
                        list_items.append(line.rstrip())
                    for l, item in enumerate(sorted(list_items, key=str.lower), start=1):
                        print("{0:>{2}}: {1}".format(str(l), item, (lambda: 1 if len(list_items) < 10 else 2
                                                                                if len(list_items) < 100 else 3)()))
                except EnvironmentError as err:
                    print("ERROR", err)
                finally:
                    saved = True
                    action_items = get_string("[A]dd [D]elete [Q]uit ", "add_string", default="a")
                continue
            elif action_items in {"q", "Q"}:  # выход из программы
                if saved:
                    break
                elif not saved:
                    answer = get_string("Saved unseved changes (y/n)", "answer", default="y")
                    if answer in {"y", "Y"}:
                        fh = open(file_name, "w", encoding="utf-8")
                        for l, item in enumerate(list_items, start=1):
                            fh.write("{1}\n".format(l, item))
                        print("Saved {0} items to {1}".format(l, file_name))
                        fh.close()
                        break
                    else:
                        break
                else:
                    break
            else:
                print("ERROR: invalid choice--enter one of 'AaDdSsQq'")
                action_items = get_string("Press Enter to continue...", "add_string")
                if action_items is not None:
                    action_items = get_string("[A]dd [D]elete [S]ave [Q]uit ", "add_string", default="a")
        except ValueError as err:
            print(err)


def main():
    while True:
        list_files = [name for name in os.listdir(".") if name.endswith(".lst")]
        if len(list_files) == 0:
            filename = add_new_file_name()
            read_record_file(filename, action_items="a")
        else:
            for n, file in enumerate(list_files, start=1):
                print("{0:>{2}}: {1}".format(str(n), file, (lambda: 1 if len(list_files) < 10 else 2
                                                                                if len(list_files) < 100 else 3)()))
            number_file = get_integer("Choose number or '"'0'"' for add new file ", "number_file")
            if number_file == 0:
                filename, action_asw = add_new_file_name()
                read_record_file(filename, action_asw)
            else:
                if os.stat(list_files[number_file-1]).st_size == 0: 
                    filename, action_asw = add_new_file_name(list_files[number_file-1])
                    if action_asw in {"A", "a"}:
                        read_record_file("".join(list_files[number_file-1]), action_items="a")
                        break
                    else:
                        break
                else:
                    read_record_file("".join(list_files[number_file-1]), action_items="o")
                    break
main()
