# Stock News Signal Analyzer

## Overview

Stock News Signal Analyzer is a project that retrieves news for a given list of securities, analyzes the news for investment signals, and outputs the results to an Excel file. It also stores the news in a JSON file. This project leverages the SymbolicAI framework and SerpApi for news retrieval and analysis.

## Features

- Retrieve news articles for a list of securities using SerpApi.
- Fetch full article content from the web.
- Summarize the article content using SymbolicAI.
- Analyze the summarized news articles to generate investment signals (buy, sell, hold).
- Save the analysis results in an Excel file.
- Store the news articles in a JSON file with a timestamp.

## Setup

### Prerequisites

- SerpApi Key (set as environment variable `SERP_API_KEY`)
- OpenAI API Key (set as environment variable `OPENAI_API_KEY`)


### Installation

1. Clone the repository:
   ```
   git clone https://github.com/sumit1717/stock-News-Signal-Analyzer.git
   cd stock-News-Signal-Analyzer
2.  Install dependencies:
    ```
    pip install -r requirements.txt
3. Set the SERP_API_KEY and OPENAI_API_KEY environment variables with your respective API keys:
    ```
    export SERP_API_KEY='your_serpapi_key'
    export OPENAI_API_KEY='your_openai_key'
   
## Usage
Run the main script to retrieve and analyze news, then save the results:
    
    python main.py

## Configuration
Modify config.py to update the list of securities or to set API keys:

    SERP_API_KEY = os.getenv('SERP_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    SYMBOLIC_AI_ENGINE = 'gpt-4'
    SECURITIES = ['AAPL', 'GOOGL', 'AMZN']  # Example securities