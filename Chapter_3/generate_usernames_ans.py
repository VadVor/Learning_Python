import collections
import sys


ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)
User = collections.namedtuple("User", "username forename middlename surname id")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "-help"}:
        print("usage: {0} file1 [file2 [...fileN]]".format(sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                users[(user.surname.lower(), user.forename.lower(), user.id)] = user
    print_users(users)


def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    return user


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username


def print_users(users):
    namewidth = 17
    usernamewidth = 9
    list_for_print = []
    head1="{0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=namewidth, uw=usernamewidth)
    head2="{0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=namewidth, uw=usernamewidth)
    print(head1+'   '+head1)
    print(head2+'   '+head2)
    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname}, {0.forename}{1}".format(user, initial)
        langth_name = len(name)
        if langth_name<=17:
            list_for_print.append("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(name, user, nw=namewidth, uw=usernamewidth))
        else:
            list_for_print.append("{0:.{nw}} ({1.id:4}) {1.username:{uw}}".format(name, user, nw=namewidth, uw=usernamewidth))
    j = 0
    for t in zip(list_for_print[1::2],list_for_print[::2]):
        if j <= 61: 
            print('   '.join(t))
            j+=1
        else:
            print('\f')
            print(head1+'   '+head1)
            print(head2+'   '+head2)
            print('   '.join(t))
            j=0

main()

