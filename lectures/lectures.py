import json
import pandas as pd

with open('lectures/lectures.json', encoding='UTF-8') as data_file:    
    data = json.load(data_file) 


def convert(data):
    out = []
    tab = '--'
    def convert_menu(data,level):
        for i in data:
            value = data[i]
            out.append('<details><summary>'+ tab*level+i + '</summary>')
            if type(value) == list:            
                for j in value:
                    convert_menu(j,level+1)
                    out.append('</details>')
            else:
                out.append('<blockquote>' + tab*level + value + '</blockquote>')

    convert_menu(data,0)            
    return out

result = convert(data)

with open('lectures/lectures.md','w+') as out_file:
    out_file.write('\n')
    for r in result:
        out_file.write(r)
