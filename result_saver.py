import pandas as pd
import json
from datetime import datetime


class ResultSaver:
    @staticmethod
    def save_to_excel(data, filename='investment_signals.xlsx'):
        try:
            df = pd.DataFrame(data)
            df.to_excel(filename, index=False)
        except Exception as e:
            print(f"Error saving to Excel: {e}")

    @staticmethod
    def save_to_json(security_ticker, news_articles, filename='news_data.json'):
        news_data = {
            "ticker": security_ticker,
            "timestamp": datetime.now().isoformat(),
            "articles": news_articles
        }
        try:
            with open(filename, 'w') as file:
                json.dump(news_data, file, indent=4)
        except Exception as e:
            print(f"Error saving to JSON: {e}")
