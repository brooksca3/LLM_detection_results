import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia New Pages
url = "https://el.wikipedia.org/w/index.php?title=%CE%95%CE%B9%CE%B4%CE%B9%CE%BA%CF%8C:%CE%9D%CE%AD%CE%B5%CF%82%CE%A3%CE%B5%CE%BB%CE%AF%CE%B4%CE%B5%CF%82&limit=5000"

response = requests.get(url)
response.raise_for_status() # Raises an HTTPError for bad responses

# Parsing the content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all list items that contain new page entries
new_pages = soup.find_all('li', {'data-mw-revid': True})
pages_found = []
st_head = 'https://en.wikipedia.org/'
# Extracting and printing the first link from each list item
for page in new_pages:
    first_link = page.find('a', href=True)
    if first_link:
        print(first_link['href'])
        pages_found.append(st_head + first_link['href'])


#######

for ind,url in enumerate(pages_found):
    response = requests.get(url)
    response.raise_for_status() # Check for HTTP request errors

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the main content text div and extract text from <p> tags
    content_text = soup.find('div', {'class': 'mw-parser-output'})
    paragraphs = content_text.find_all('p') if content_text else []
    cur_string = ""
    # print(f"Text from {url}:")
    for p in paragraphs:
        print(p.get_text())
        cur_string += p.get_text() + '\n'
    with open(f'files/el1_{ind}.txt','w') as f:
        f.write(cur_string)
    # print("\n---\n")