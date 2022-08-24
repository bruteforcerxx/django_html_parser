'''
This script is a converter for ordinary html files to django-readable html files.
The aim of this script is to further reduce development and integration time for django-backend developers.

Your html file must exist in same directory as script

<-USAGE->
conv = Converter('index.html')
conv.read_html()
conv.parse_to_django()
conv.save_to_html()

if the script runs successfully, a directory named html_django will be created. and inside this directory, your django-readable
html file can be found.

NOTE: You may or may not get an error while running the save_to_html() method. In a case where you encounter an error,
you should edith the directory path variable in this method to point to a valid file directory.

Author: Michael Olu
'''

import os


class Converter:
    def __init__(self, filename):
        self.filename = filename
        self.html_string = ''

    def __repr__(self):
        return f'<Html-Django parser Object>'

    def read_html(self):
        data = self.filename
        try:
            text_file = open(data, "r")
            data_content = text_file.read()
            text_file.close()
            self.html_string = data_content
            return f'<reader method for Html-Django parser Object>'
        except Exception as e:
            print(e)

    def parse_to_django(self):
        a = self.html_string

        a = a.replace('<!DOCTYPE html>', """<!DOCTYPE html> 
        {% load static %}""")
        a = a.replace('<!doctype html>', """<!DOCTYPE html> 
        {% load static %}""")
        a = a.replace('href="', """href="{% static '""")
        a = a.replace('src="', """src="{% static '""")
        a = a.replace('action="', """action="{% url '""")

        a = a.replace(""".css">""", """.css' %}">""")
        a = a.replace(""".js">""", """.js' %}">""")

        a = a.replace(""".jpeg""", """.jpeg' %}">""")
        a = a.replace(""".jpg""", """.jpg' %}""")
        a = a.replace(""".png""", """.png' %}""")
        a = a.replace(""".svg""", """.svg' %}""")

        a = a.replace(""".html""", """' %}""")
        a = a.replace("""#""", """ ' %}""")
        a = a.replace('<a href="{% static', '<a href="{% url')
        self.html_string = a
        return f'<converter method for Html-Django parser Object>'

    def save_to_html(self):
        try:
            data = self.html_string
            try:
                # Edit the file path to point to a valid directory if you encounter any error
                path = f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\django_html_parser\html_django'
                os.mkdir(path)
            except Exception as e:
                print(f'{e}, please edit the path variable to point to a valid directory.')
                pass
            text_file = open(f"html_django/{self.filename}", "w")
            text_file.write(data)
            text_file.close()
            return f'<saver method for Html-Django parser Object>'
        except Exception as e:
            return e


# filename = input('Enter file name eg: index.html:->')

conv = Converter('index.html')
print(conv.read_html())
print(conv.parse_to_django())
print(conv.save_to_html())
