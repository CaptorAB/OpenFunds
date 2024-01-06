from bs4 import BeautifulSoup
import re
import unicodedata

def remove_head_tags(input):

    # Parse the HTML
    soup = BeautifulSoup(input, 'html.parser')

    # Find and remove all <head> tags
    for head_tag in soup.find_all('head'):
        head_tag.decompose()

    return str(soup)

def remove_inline_styles(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove inline styles
    for tag in soup.find_all(style=True):
        del tag['style']

    # Find and remove <span> tags with variable number of �
    for span_tag in soup.find_all('span', string=re.compile('\W*�+\W*')):
        span_tag.decompose()

    for tag in soup.find_all(attrs={"class": "MsoNormal"}):
        del tag['class']

    # Clean up newline and extra whitespace in <span> elements
    #for span_tag in soup.find_all('span'):
    #    if span_tag.string:
    #        span_tag.string.replace_with(span_tag.get_text().replace('\n', ' ').strip())

    for element in soup.find_all(text=True):
        new_text = re.sub(r'\n\s+', ' ', element)
        element.replace_with(new_text)
                
    return str(soup)


with open('fieldlist.htm', 'r') as file:
    html_content = file.read()



text = remove_head_tags(html_content)
text = remove_inline_styles(text)

text = unicodedata.normalize('NFKD', text)

with open('cleaned_html_file.html', 'w') as file:
    file.write(text)
