import json
import sys

json_file = sys.argv[1]
md_file = sys.argv[2]

with open(json_file, encoding='UTF-8') as data_file:    
    data = json.load(data_file) 

text_style = 'style="font-size:200%;cursor: pointer;padding: 10px;"'
heading_style = 'style="font-size:200%;cursor: pointer;"'

def convert(data):
    out = []
    tab = '&emsp;'
    def convert_menu(data,level):
        for i in data:
            value = data[i]
            out.append(f'<details><summary {heading_style}>{tab*level+i }</summary>')
            if type(value) == list:            
                for j in value:
                    convert_menu(j,level+1)
                    out.append('</details>')
            else:
                if type(value) == dict:
                    for key in list(value.keys()):
                        txt = f'<blockquote {text_style}>'
                        txt +=  tab*(level + 1)
                        txt += f'<a target="_blank" href={value.get(key)}>{key}</a>'
                        txt += '</blockquote>'
                        out.append(txt)
                else:
                    out.append(f'<blockquote {text_style}>{tab*(level+1) + value}</blockquote>')

    convert_menu(data,0)            
    return out

result = convert(data)

with open(md_file,'w+',encoding='UTF-8') as out_file:
    for r in result:
        out_file.write(r+'\n')
