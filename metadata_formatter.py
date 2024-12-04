from openai import OpenAI
import page_fetcher
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
            {"role": "system", "content": "The text provided will mostly be in norwegian, so will your following instructions. Du vil bli gitt en annonsebeskrivelse på ukjent format for datamaskiner. Du skal formatere denne annonsebeskrivelsen til json format og returnere det, BARE json formatet. De følgende elementene skal ALLTID returneres, men de kan settes til \"unknown\" hvis de ikke har noen info. De følgende feltene er; \"PRICE\", \"CPU\", \"GPU\", \"MEMORY\", \"STORAGE\", \"POWER_SUPPLY\", \"WIFI_CARD\""},
            {"role": "user", "content": metadata}
        ]
    )

    raw_content = completion.choices[0].message.content

    # Remove code block markers (```json ... ```)
    clean_content = raw_content.strip("```json").strip()

    # Parse JSON content into a Python dictionary
    formatted_json = json.loads(clean_content)

    print(formatted_json)



if __name__ == "__main__":
    json_formatter("https://www.finn.no/recommerce/forsale/item/383416513")