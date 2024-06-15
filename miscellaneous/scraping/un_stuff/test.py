from scrape_press_release import scrape_press_release

urls = [
    "https://afghanistan.un.org/en/243763-unfao-receives-funding-japan-support-community-based-irrigation-enhanced-agricultural",
    "https://afghanistan.un.org/en/238813-un-launches-new-strategic-framework-supporting-afghan-people",
]

for url in urls:
    print(scrape_press_release(url))
    print("\n\n\n")


