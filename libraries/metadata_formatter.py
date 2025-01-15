from openai import OpenAI
from libraries import page_fetcher
# import page_fetcher
from dotenv import load_dotenv
import os, json

load_dotenv()

def json_formatter(url):

    metadata = page_fetcher.metadata_fetcher(url)
    # print(metadata)

    api_key = os.getenv('API_KEY')

    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "The text provided will mostly be in norwegian, so will your following instructions. Du vil bli gitt en annonsebeskrivelse på ukjent format for datamaskiner. Du skal formatere denne annonsebeskrivelsen til json format og returnere det, BARE json formatet. Det er veldig viktig du finner og returnerer \"PRICE\", altså prisen på datamaskinene, denne vil alltid være oppgit i norske kroner så du kan bare returnere et heltall for prisen. De følgende elementene skal ALLTID returneres, men de kan settes til \"unknown\" hvis de ikke har noen info. De følgende feltene er; \"PRICE\", \"CPU\", \"GPU\", \"MEMORY\", \"STORAGE\", \"POWER_SUPPLY\", \"WIFI_CARD\""},
            {"role": "user", "content": metadata}
        ]
    )

    raw_content = completion.choices[0].message.content

    # Remove code block markers (```json ... ```)
    clean_content = raw_content.strip("```json").strip()

    # Parse JSON content into a Python dictionary
    formatted_json = json.loads(clean_content)

    print(formatted_json)
    return formatted_json


def jsonSave(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def jsonLoad(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    list_of_urls = jsonLoad("fetched_links.json")

    for i in list_of_urls:
        json_formatter(i)