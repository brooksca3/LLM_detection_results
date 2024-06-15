import wikipediaapi

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

    return text_content

# Example usage:
page_title = 'Konstanz-Fürstenberg station'
article_text = scrape_wikipedia_article(page_title)

if article_text:
    print(article_text)
