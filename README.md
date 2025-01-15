# Finn.no Computer Deals Analyzer

## Overview

The **Finn.no Computer Deals Analyzer** is a Python-based automated system designed to scour Finn.no for computer listings, evaluate their specifications, and identify the best deals. By leveraging GPT-3.5 for data parsing and decision-making, this tool ensures that only the most relevant and cost-effective options make it to your final review. 

### Key Features:
- **Automated Finn.no Listings Scraper**: Pulls raw listings of computers from Finn.no.
- **AI-Powered Data Parsing**: Utilizes GPT-3.5 to transform raw listing data into a standardized JSON format of computer specifications.
- **Smart Filtering**: Removes irrelevant or low-quality listings based on your criteria.
- **Tournament-Style Evaluation**: Puts listings against each other in brackets, where GPT-3.5 determines the better deal in each round, ultimately selecting five finalists.
- **Final Review**: Presents the top 5 options for manual evaluation to ensure satisfaction.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/filip-rs/finn-scraper.git
   cd finn-scraper
   ```

2. **Set Up the Environment**:
   - Ensure Python 3.9+ is installed.
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv env
     source env/bin/activate # On Windows: env\Scripts\activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**:
   - Obtain an OpenAI API key
   - Create a `.env` file in the root directory and add:
     ```env
     API_KEY=xx-xxxxxxxxxxxxxxxxxxxxxxxxx
     ```

---

## Usage

1. **Run the Script**:
   ```bash
   python main.py
   ```

2. **Process Flow**:
   - **Step 1**: The script scrapes Finn.no for computer listings based on your search criteria.
   - **Step 2**: GPT-3.5 processes raw data into structured JSON specifications.
   - **Step 3**: Listings are filtered to remove irrelevant or low-value options.
   - **Step 4**: A tournament-style elimination determines the best deals.
   - **Step 5**: The final 5 candidates are displayed for manual review.

3. **Output**:
   - The script generates a detailed report of the finalists in both JSON and plain-text formats for easy access.

---

## Configuration

To customize the behavior:
- **Runtime**: Certain options are available at runtime, such as search query.
- **Additional customisation**: Most of the programs logic is located in `main.py` and can be modified there.

---

## Example Output

### JSON Output
```json
{
    "PRICE": $$$$,
    "CPU": "AMD Ryzen 7 2700X",
    "GPU": "MSI Radeon RX 5700 XT 8GB",
    "MEMORY": "Corsair Vengeance 3600 mhz 16 RGB",
    "STORAGE": "1 TB M.2 NVMe",
    "POWER_SUPPLY": "Sharkoon WPM 600 Bronze",
    "WIFI_CARD": "ROG CROSSHAIR VII HERO (WI-FI)",
    "url": "https://www.url.com"
}
```

### Finalists
1. Dell XPS 15 2022 - $1200 - {url}
2. HP Spectre x360 - $1100 - {url}
3. Lenovo ThinkPad X1 Carbon - $1300 - {url}
4. Apple MacBook Pro 14" - $2000 - {url}
5. ASUS ROG Zephyrus G14 - $1400 - {url}

---

## Dependencies

- **Python Packages**:
  - `requests==2.32.3`: For interacting with APIs.
  - `beautifulsoup4==4.12.3`: Scraping Finn.no listings.
  - `openai==1.56.1`: OpenAi API integration.
  - `python-dotenv==1.0.1`: Managing environment variables, more specifically the API key.

Install them with:
```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome! If you’d like to improve the system or add features, feel free to fork the repository and submit a pull request.

---

## Limitations

- The script relies on GPT-3.5, which does cost money. It is however reasonably priced but beware.
- Performance may vary based on the quality of the Finn.no data and GPT-3.5's parsing capabilities. GPT can and will make mistakes.

---

## License

![MIT License](https://img.shields.io/badge/license-MIT-green)

---

## Acknowledgments

- **OpenAI GPT-3.5**: For its text parsing and decision-making capabilities.
- **Contributors**: Thank you to me, myself and I.