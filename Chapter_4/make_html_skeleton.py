import datetime
import xml.sax.saxutils


COPYRIGHT_TEMPLATE = "Copyright (c) {0} {1}. All rights reserved."
STYLESHEET_TEMPLETE = ('<link rel="stylesheet" type="text/css" '
                       'media="all" href="{0}" />\n')
HTML_TEMPLATE = """<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" \
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>{title}</title>
<!-- {copyright} -->
<meta name="Description" content="{description}" />
<meta name="Keywords" content="{keywords}" />
<meta equiv="content-type" content="text/html; chatset=utf-8" />
{stylesheet}\
</head>
<body>
</html>
"""

class CancelledError(Exception): pass

def main():
    information = dict(name=None, year=datetime.date.today().year, filename=None, title=None, description=None,
                       keywords=None, stylesheet=None)
    while True:
        try:
            print("\nMake HTML Skeleton\n")
            populate_information(information)
            make_html_skeleton(**information)
        except CancelledError:
            print("Cancelled")
        if get_string("\nCreate another (y/n)?", default="y").lower() not in {"y", "yes"}:
            break

def populate_information(information):
    name = get_string("Enter your name (for copyright)", "name", information["name"])
    if not name:
        raise CancelledError()
    year = get_integer("Enter copyright year", "year", information["year"], 2000, datetime.date.today().year+1, True)
    if year == 0:
        raise CancelledError()
    filename = get_string("Enter filename", "filename",)
    if not filename:
        raise CancelledError()
    if not filename.endswith((".htm", ".html")):
        filename += ".html"
    information.update(name=name, year=year, filename=filename, title=title, description=description,
                       keywords=keywords, stylesheet=stylesheet)

