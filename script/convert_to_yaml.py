#/bin/env python3

import argparse
from pprint import pprint
import yaml
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser("convert_to_yaml")
    args, unknown_args = parser.parse_known_args()

    html_content = ""
    with open("cleaned_html_file.html", encoding="utf-8") as file_handle:
       html_content =  file_handle.read()


    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Function to extract text from a span tag sequence
    def extract_text(tag_sequence):
        try:
            return ''.join([tag.get_text(strip=True) for tag in tag_sequence])
        except:
            return ""

    # Find all list items
    list_items = soup.find_all('li')

    data_list = []

    cnt = 0

    for item in list_items:
        # Extracting various pieces of information
        of_id = extract_text(item.find('b'))

        field_name_tags = item.find_all('span', string='Field Name')[0].find_next_siblings('span')
        field_name = extract_text(field_name_tags)

        field_level_tags = item.find_all('span', string='Field Level')[0].find_next_siblings('span')
        field_level = [tag.get_text(strip=True) for tag in field_level_tags]

        data_type_tags = item.find('span', string='Data Type').find_next_sibling('span')
        data_type = extract_text(data_type_tags)

        introduced, revoked = extract_text(item.find('span', string='Introduced / Revoked').find_next_siblings('span')).split("/")
        
        description = ""
        start_tag = item.find('span', string='Description')
        end_tag = item.find('span', string='Values')

        current_tag = start_tag
        while current_tag:            
            if current_tag == end_tag:
                break

            if current_tag != start_tag and current_tag != end_tag:
                print(current_tag.get_text())
                description = description + current_tag.get_text() 

            current_tag = current_tag.find_next()

        #description = description.replace("\n", " ")
        description = re.sub(r'\s+', ' ', description)
        description = description.replace(".pnghttps://www.", ".png https://www.")

        values_tags = item.find('span', string='Values').find_next_siblings('span')
        values = extract_text(values_tags)

        example_tags = item.find('span', string='Example').find_next_sibling('span')
        example = extract_text(example_tags)


        data_list.append({
            'OFID': of_id,
            'FieldName': field_name,
            'FieldLevel': field_level,
            'DataType': data_type,
            'Introduced': introduced.strip(),
            'Revoked': revoked.strip(),
            'Description': description.strip(),
            'Values': values,
            'Example': example.strip()
        })

        #cnt = cnt + 1
        #if cnt >2:
        #    break


    #print(yaml.dump(data_list, width=80))
    
    with open('fieldlist.yaml', 'w') as file:
        yaml.dump(data_list, file, width=80)





