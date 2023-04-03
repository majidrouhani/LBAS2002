import json
import sys

json_file = sys.argv[1]
md_file = sys.argv[2]

with open(json_file, encoding='UTF-8') as data_file:    
    data = json.load(data_file) 


def convert(data):
    out = []
    tab = '--'
    def convert_menu(data,level):
        for i in data:
            value = data[i]
            out.append('<details><summary><font size="5">' + tab*level+i + '</font></summary>')
            if type(value) == list:            
                for j in value:
                    convert_menu(j,level+1)
                    out.append('</details>')
            else:
                out.append('<blockquote><font size="5">' + tab*level + value + '</font></blockquote>')

    convert_menu(data,0)            
    return out

result = convert(data)

with open(md_file,'w+',encoding='UTF-8') as out_file:
    out_file.write('# LBAS2002 - Informatikk: Programmering\n')
    for r in result:
        out_file.write(r+'\n')
