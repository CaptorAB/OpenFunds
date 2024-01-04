#/bin/env python3

import argparse
from pprint import pprint
import yaml
import unicodedata
import re

ID_PATTERN = re.compile(r'OF-ID\W+\*\*(.*)\*\*\*\*\*\*', re.DOTALL)
ID_PATTERN = re.compile(r'OF-ID\s+\*\*(\w+?)\*\*\s+Field Name\s+\*\*(\w+)\n(\w+)\*\*\*\*\*\*', re.DOTALL)



if __name__ == "__main__":
    parser = argparse.ArgumentParser("convert_to_yaml")
    args, unknown_args = parser.parse_known_args()

    text = ""
    with open("fieldlist.initial.md", encoding="utf-8") as file_handle:
       text =  file_handle.read()

    chunks = text.split("\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_")

    fields = []

    for chunk in chunks:
        text = unicodedata.normalize('NFKD', chunk)

        m = re.search(ID_PATTERN, text)
        if re.search(ID_PATTERN, text):
            print(m)
            print(m.groups())
            fields.append({"OF-ID": m.groups()[0], "Field Name": m.groups()[1] + " " + m.groups()[2]})

        #pprint(text)

    with open("fieldlist.yaml", "w") as file:
        yaml.dump(fields, file)
