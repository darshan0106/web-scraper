import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    try:
        print("\n🔍 Fetching headlines...\n")
        response = requests.get(url)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, "html.parser")

        possible_tags = [("h1", None), ("h2", None), ("h3", None), ("h2", "headline-class")]

        headlines = []
        for tag, class_name in possible_tags:
            found = soup.find_all(tag, class_=class_name)
            if found:
                headlines.extend(found)
        
        if not headlines:
            print("⚠ No headlines found. The webpage structure might have changed.")
            return

        print("📰 Latest Headlines:\n" + "=" * 30)
        for i, headline in enumerate(headlines[:10], 1): 
            print(f"{i}. {headline.get_text().strip()}")

        print("\n✅ Done!\n")

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching the web page:", e)

# Replace with the actual website URL
url = "https://example.com"  
scrape_headlines(url)
