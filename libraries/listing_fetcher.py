import json
import requests

def jsonSave(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def jsonLoad(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def fetch_finn_listings(search_query, page_number, headers=None):
    url = "https://www.finn.no/api/search-qf"
    
    querystring = {
        "searchkey": "SEARCH_ID_BAP_COMMON",
        "q": search_query,
        "page": page_number,
        "vertical": "bap"
    }
    
    if headers is None:
        headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "nb-NO,nb;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Sec-GPC": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        
        data = response.json()
        # jsonSave("request.json", data)
        
        urls = [
            doc.get("canonical_url") 
            for doc in data.get("docs", []) 
            if doc.get("canonical_url") and "bap" not in doc.get("canonical_url")
        ]
        
        return urls
    
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return []



if __name__ == "__main__":
    search_query = "gaming pc"
    urls = fetch_finn_listings(search_query)
    
    print(f"Found {len(urls)} listings:")
    for url in urls:
        print(url)

    jsonSave("fetched_links.json", urls)