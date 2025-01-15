import json
# import libraries.listing_fetcher as listing_fetcher
# import libraries.page_fetcher as page_fetcher
# import libraries.metadata_formatter as metadata_formatter
# import libraries.ai_recommender as ai_recommender

from libraries import (
    listing_fetcher,
    metadata_formatter,
    ai_recommender
)


def main():
    reset = str(input("Do you want to reset fetched_links? Usually used when changing search query. Leave blank for no: "))

    if reset.lower() == "yes" or reset.lower() == "ja":
        jsonSave("fetched_links.json", [])
        
    search_query = str(input("Enter search query, leave blank for \"gaming pc\": "))

    if not search_query:
        search_query = "gaming pc"

    new_urls = []
    page_number = 1
    for i in range(50):
        new_urls += listing_fetcher.fetch_finn_listings(search_query, page_number)
        page_number += 1

    
    print(f"Found {len(new_urls)} listings:")
    for url in new_urls:
        print(url)

    urls = jsonLoad("fetched_links.json")

    for url in new_urls:
        if url not in urls:
            urls.append(url)

    jsonSave("fetched_links.json", urls)


    json_format = str(input("Do you want to format all the found metadata to json format? Default option is yes: "))
    if not json_format:
        json_format = "yes"

    
    if json_format.lower() == "yes" or json_format.lower() == "ja":
        
        alternatives = []
        for url in urls:
            alternatives.append(metadata_formatter.json_formatter(url))

    for alternative, url in zip(alternatives, urls):
        alternative['url'] = url

    jsonSave("data.json", alternatives)

    ai_response = ai_recommender.recommendation(alternatives)

    print(ai_response)
    jsonSave("response.json", ai_response)


def jsonSave(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def jsonLoad(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    main()
