import os
import sys
import json

#converts from a directory json files in xml and puts the new files in a new directory

def json2xml(json_obj, line_padding=""):
    result_list = list()

    json_obj_type = type(json_obj)
    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json2xml(sub_elem, line_padding))

        return "\n".join(result_list)

    if json_obj_type is dict:
        result_list.append('<Immobile>')
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("%s<%s>" % (line_padding, tag_name))
            result_list.append(json2xml(sub_obj, "\t" + line_padding))
            result_list.append("%s</%s>" % (line_padding, tag_name))
        result_list.append('</Immobile>')
        return "\n".join(result_list)
        
    
    return "%s%s" % (line_padding, json_obj)
    
try:
    if __name__ == "__main__":
        jsonInput=sys.argv[1]
        destination_dir=sys.argv[2]

        for subdir, dirs, files in os.walk(jsonInput):
            for file in files:
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)
                output = open(destination_dir+'/'+os.path.basename(file).split('.')[0]+'.xml', 'w')
                output.write(json2xml(json.load(open(subdir+'/'+file, 'r'))))

except IndexError:
    print('Wrong arguments. There are 2: directory with json files, new directory')