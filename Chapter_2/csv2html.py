import sys
from xml.sax.saxutils import escape


def main():
        formatt = process_options()
        if (formatt[0] and formatt[1]) is None:
            return None
        else:
            print_start(formatt)
            count = 0
            filename = formatt[2]
            file = open(filename, "r")
            for line in file.readlines():
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, formatt)
                count += 1
        print_end(formatt)


def print_start(formatt):
    filename = formatt[3]
    with open(filename, "w") as file:
        file.write("<table border='1'>")
        file.close()


def print_line(line, color, formatt):
    filename = formatt[3]
    with open(filename, "a") as file:
        file.write("<tr bgcolor='{0}'>".format(color))
        numberformat = "<td align='right'>{{0:{0}}}</td>".format(formatt[1])
        fields = extract_fields(line)
        for field in fields:
            if not field:
                file.write("<td></td>")
            else:
                number = field.replace(",", "")
                try:
                    x = float(number)
                    file.write(numberformat.format(x))
                except ValueError:
                    field = field.title()
                    field = field.replace(" And ", " and ")
                    if len(field) <= int(formatt[0]):
                        field = escape(field)
                    else:
                        field = "{0} ...".format(
                                escape(field[:int(formatt[0])]))
                    file.write("<td>{0}</td>".format(field))
        file.write("</tr>")
        file.close()


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:  # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",":  # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def process_options():
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h", "--help"):
            print("usage:"
                  "csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html" + '\n' +
                  "maxwidth is an optional integer; if specified, it sets the maximum"
                  "number of characters that can be output for string fields,"+ '\n' +
                  "otherwise a default of 100 characters is used."+ '\n' +
                  "(maxwidth – необязательное целое число. Если задано, определяет"
                  "максимальное число символов для строковых полей. В противном случае"+ '\n' +
                  "используется значение по умолчанию 100.)"+ '\n' +
                  "format is the format to use for numbers; if not specified it defaults to '.0f'"+ '\n' +
                  "(format – формат вывода чисел. Если не задан, по умолчанию используется формат '.0f'.)")
            forma = (None, None)
            return forma
        elif len(sys.argv) == 5:
            forma = (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
            return forma
        elif len(sys.argv) == 3:
            forma = (100, ".0f", sys.argv[1], sys.argv[2])
            return forma


def print_end(formatt):
    filename = formatt[3]
    with open(filename, "a") as file:
        file.write("</table>")
        file.close()

main()
