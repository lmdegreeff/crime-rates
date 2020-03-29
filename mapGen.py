import pandas
import codecs

path = 'map.html'
template = codecs.open(path, 'r', 'utf-8');
contents = template.read()
template.close

import os

path = '/crime-rates'
os_info = os.walk(path)
for roots, dirs, files in os_info:
    coord_dir = files

for file in coord_dir:
    coord_file = open('location of file', 'r')
    coords = coordfile.read()
    coord_file.close()
    lines = contents.splitlines()
    first = '\n'.join(lines[0:103])
    last = '\n'.join(lines[103:])
    for line in coords.splitlines():
        first += '\t\t\t' + line + '\n'
    html_string = first + last
    file_name = file.replace('.txt', '')
    template = open('location of file directory' + file_name + '_map.html', 'w+')
    template.write(html_string)
    template.close()
