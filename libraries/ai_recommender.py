from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

def recommendation(content):
    api_key = os.getenv('API_KEY')

    client = OpenAI(api_key=api_key)
    # Convert alternatives list to a JSON string
    content_str = json.dumps(content, ensure_ascii=False, indent=4)
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "The following content will be various json lists containing information about different deals on \"Finn.no\" the norwegian website. Priser vil bli oppgitt som et tall, og er gitt i NOK (kroner). Du skal sammenlikne spesifikasjoner og avgjøre hvilke alternativ som gir den beste dealen til brukeren. Du kan da forklare hvilken deal som er best og hvorfor den ble valgt. Du kan også gi en topp 3 hvis det finnes flere alternativ. Noen av alternativene vil ha verdier gitt som \"unknown\", her kan du i noen tilfeller anta verdier ettersom brukeren kan manuelt sjekke disse verdiene i ettertid. Hovedfokus skal legges på hvilket kjøp som er mest \"undervalued\" og kan gi mest profitt hvis den skal selges senere: "},
            {"role": "user", "content": content_str}
        ]
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    alternatives = [{'PRICE': 'unknown', 'CPU': 'Intel core i5 7600k', 'GPU': 'Zotac gtx 1660ti', 'MEMORY': 'Kingston 8gb ram', 'STORAGE': 'Kingston 120gb ssd, Western Digital blue 1tb hdd', 'POWER_SUPPLY': 'Corsair 850w', 'WIFI_CARD': '300kr ekstra for wifi adapter'},
                    {'PRICE': 'unknown', 'CPU': 'AMD Ryzen 7 2700X 8 kjerner, 16 tråder', 'GPU': 'MSI Radeon RX 5700 XT 8GB', 'MEMORY': 'Corsair Vengeance 3600 mhz 16 RGB', 'STORAGE': '1 TB M.2 NVMe', 'POWER_SUPPLY': 'Sharkoon WPM 600 Bronze', 'WIFI_CARD': 'ROG CROSSHAIR VII HERO (WI-FI)'},
                    {'PRICE': 'unknown', 'CPU': 'Intel core i7 7700', 'GPU': 'ASUS strix gtx 1060', 'MEMORY': '16gb', 'STORAGE': 'Kingston 1tb m.2 ssd', 'POWER_SUPPLY': 'Corsair tx750w', 'WIFI_CARD': 'unknown'},
                    {'PRICE': 'MONT3699', 'CPU': 'Intel core i5 8400', 'GPU': 'Gigabyte gtx 1080', 'MEMORY': 'Kingston 16gb ram', 'STORAGE': 'Western Digital 256gb m.2 ssd, Seagate 1tb hdd', 'POWER_SUPPLY': 'Cheiftec 750w', 'WIFI_CARD': 'unknown'},
                    {'PRICE': 'unknown', 'CPU': 'unknown', 'GPU': 'unknown', 'MEMORY': 'unknown', 'STORAGE': 'unknown', 'POWER_SUPPLY': 'unknown', 'WIFI_CARD': 'unknown'},
                    {'PRICE': 'unknown', 'CPU': 'Ryzen 5 7500f', 'GPU': 'Rtx 3070 trubo', 'MEMORY': '16gb ddr5 ram', 'STORAGE': '1tb ssd', 'POWER_SUPPLY': 'Corsair psu 750w', 'WIFI_CARD': 'unknown'},
                    {'PRICE': 'unknown', 'CPU': 'AMD Ryzen 5 3600', 'GPU': 'GeForce GTX 1070', 'MEMORY': '16GB Corsair Vengeance RGB PRO DDR4 3200MHz', 'STORAGE': 'Kingston M.2 SSD 1TB', 'POWER_SUPPLY': '650W', 'WIFI_CARD': 'unknown'},
                    {'PRICE': 'unknown', 'CPU': 'i5-8400', 'GPU': 'geforce rtx 1060', 'MEMORY': '16gb', 'STORAGE': 'unknown', 'POWER_SUPPLY': 'unknown', 'WIFI_CARD': 'unknown'},
                    {'PRICE': 'unknown', 'CPU': 'i7 3770k', 'GPU': 'GTX 970 4GB', 'MEMORY': '24GB Corsair Vengance (2x8GB+2x4GB)', 'STORAGE': 'SSD: 120GB Samsung, HDD: 1TB Samsung', 'POWER_SUPPLY': 'CX500', 'WIFI_CARD': 'Trådløst USB nettverkskort'},
                    {'PRICE': 'unknown', 'CPU': 'Intel(R) Core i5-7600K', 'GPU': 'NVIDIA GeForce GTX 1070', 'MEMORY': '16GB (2 x 8GB Vengeance LPX DDR4)', 'STORAGE': '500GB SSD (Kingston NV2)', 'POWER_SUPPLY': 'Corsair CX650M - 650 watt', 'WIFI_CARD': 'Bluetooth adapter (damaged)'},
                    {'PRICE': 'unknown', 'CPU': 'Intel core i5-2500k', 'GPU': 'Nvidia geforce GTX 970', 'MEMORY': '16gb ram', 'STORAGE': 'unknown', 'POWER_SUPPLY': 'unknown', 'WIFI_CARD': 'unknown'},
                    {'PRICE': 'unknown', 'CPU': 'unknown', 'GPU': 'unknown', 'MEMORY': 'unknown', 'STORAGE': 'unknown', 'POWER_SUPPLY': 'unknown', 'WIFI_CARD': 'unknown'},
                    {'PRICE': '23000 kr', 'CPU': 'AMD RYZEN 5 7600', 'GPU': 'AMD 6800XT', 'MEMORY': '32 Gb', 'STORAGE': '1TB', 'POWER_SUPPLY': 'Corsair RM 750e', 'WIFI_CARD': 'unknown'},
                    {'PRICE': 'unknown', 'CPU': 'unknown', 'GPU': '2060', 'MEMORY': 'unknown', 'STORAGE': '250gb', 'POWER_SUPPLY': 'unknown', 'WIFI_CARD': 'unknown'},
                    {'PRICE': 'unknown', 'CPU': 'Intel Core I7-6700k - Turbo 4,2 GHz - 4 core, 8 thread', 'GPU': 'Gigabyte GeForce GTX 1060 3G - 3 GB GDDR5', 'MEMORY': '8 GB - Kingston HyperX - 2400MHz (2x4 GB)', 'STORAGE': '256 GB Samsung 950 Pro M.2 NvMe + 1 TB - Seagate Barracuda - 7200rpm - HDD', 'POWER_SUPPLY': 'unknown', 'WIFI_CARD': 'Wifi usb-pinne (trådløst nettverk)'}]
    response = recommendation(alternatives)

    print(response)