import requests, re
from bs4 import BeautifulSoup



def metadata_fetcher(url):
    url = url
    html_content = fetch_finn_listing(url)
    
    if html_content:
        extracted_info = extract_finn_listing_info(html_content)
        
        # print("Metadata:")
        metadata = []
        for key, value in extracted_info['metadata'].items():
            # print(f"dicts: {key}: {value}")
            metadata.append(value)

        metadata.append(price_fetcher(url))
        # print(metadata)
        return str(metadata)



def price_fetcher(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the price
        price = soup.find("div", class_="h2")
        if not price:
            price2 = soup.find("p", class_="m-0 h2")
            if price2:
                # Extract the text and replace '&nbsp;' if needed
                price_text = str(price2) #.get_text() # .replace("&nbsp;", "")
                # print(price_text)
                price = price_text.replace("\xa0", " ")

        html_string = str(price)
        cleaned_string = re.sub(r'<.*?>', '', html_string)
        #cleaned_string = price
        # print(cleaned_string)

        price = f"\nPrice: {cleaned_string}"

        return price

    else:
        print("Failed to retrieve the webpage.")
        return "\nPrice not found"

    



def fetch_finn_listing(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the listing: {e}")
        return None

def extract_finn_listing_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract metadata
    metadata = {
        'title': soup.find('title').text if soup.find('title') else None,
        'description': soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else None,
    }
    
    
    return {
        'metadata': metadata,
    }



if __name__ == "__main__":
    metadata_fetcher("https://www.finn.no/recommerce/forsale/item/383416513")