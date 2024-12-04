import requests
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

        return str(metadata)




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