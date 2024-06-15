import requests
from bs4 import BeautifulSoup
import wikipediaapi
import json
from tqdm import tqdm

def get_recent_articles(url, limit=10000):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    articles = []
    while len(articles) < limit:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        ul_tag = soup.find('ul', class_='mw-contributions-list')

        if ul_tag is None:
            print("Failed to find the list of articles.")
            break

        for li_tag in ul_tag.find_all('li'):
            a_tag = li_tag.find('a', class_='mw-newpages-pagename')
            if a_tag:
                article_title = a_tag['title']
                article_url = 'https://en.wikipedia.org' + a_tag['href']
                articles.append((article_title, article_url))
                if len(articles) >= limit:
                    break

        # Find the next page link
        next_link = soup.find('a', class_='mw-nextlink')
        if next_link:
            url = 'https://en.wikipedia.org' + next_link['href']
        else:
            break

    return articles[:limit]

def scrape_wikipedia_article(page_title):
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='MyProjectName (youremail@example.com)',
        language='en'
    )

    page = wiki_wiki.page(page_title)

    if not page.exists():
        print(f"Page '{page_title}' does not exist.")
        return None

    # Extract the full text content
    text_content = page.text

    # Extract categories
    categories = list(page.categories.keys())

    return text_content, categories

def main():
    recent_articles_url = 'https://en.wikipedia.org/w/index.php?title=Special:NewPages&offset=&limit=50'
    article_limit = 10  # Set your desired number of articles
    articles = get_recent_articles(recent_articles_url, limit=article_limit)
    data = []

    for article_title, article_url in tqdm(articles, desc="Scraping articles"):
        content, categories = scrape_wikipedia_article(article_title)
        if content:
            data.append({
                'title': article_title,
                'url': article_url,
                'content': content,
                'categories': categories
            })

    with open('scraped_articles_with_categories.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Scraped data has been saved to 'scraped_articles_with_categories.json'")

if __name__ == "__main__":
    main()
