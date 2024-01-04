#/bin/env python3
import sys
import argparse
import datetime
from pprint import pprint
import yaml
import re
import unicodedata





if __name__ == "__main__":
    parser = argparse.ArgumentParser("convert_to_yaml")
    args, unknown_args = parser.parse_known_args()

    text = ""
    with open("fieldlist.initial.md", encoding="utf-8") as file_handle:
       text =  file_handle.read()

    chunks = text.split("\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_")

    for chunk in chunks:
        text = unicodedata.normalize('NFKD', chunk)
        pprint(text)
