import symai as ai
from symai import *
from config import SYMBOLIC_AI_ENGINE, OPENAI_API_KEY
import re


class NewsAnalyzer:
    def __init__(self):
        self.engine = ai.Engine()


    def preprocess_content(self, content):

        # Remove common boilerplate text and ads
        patterns = [
            r'Read more:',  # Example boilerplate pattern
            r'Subscribe to our newsletter',  # Another example
            r'Follow us on',  # Social media follow prompts
            r'Advertisement',  # Advertisements
            r'Click here for more',  # Clickbait
            r'© [0-9]{4}.*',  # Copyright lines
            r'All rights reserved',  # Legal disclaimers
            r'\d+ Comments',  # Comments section
            r'^\s*$',  # Empty lines
            r'\b[A-Z]{2,}\b',  # All-caps words (often acronyms or noise)
            r'\b\w{1,2}\b'  # Very short words (often noise)
        ]
        for pattern in patterns:
            content = re.sub(pattern, '', content, flags=re.IGNORECASE)

        # remove lines that are too short or too long
        cleaned_lines = []
        for line in content.split('\n'):
            line = line.strip()
            if 50 < len(line) < 500:
                cleaned_lines.append(line)
        return ' '.join(cleaned_lines)

    def evaluate_news(self, security_ticker, news_articles, retriever):
        signals = []
        for article in news_articles:
            url = article.get('link')
            if not url:
                continue
            news_content = retriever.fetch_article_content(url)
            if not news_content:
                continue

            # Preprocess the content to remove noise
            news_content = self.preprocess_content(news_content)

            # Ensure the news content length is within acceptable limits for openAI
            if len(news_content) > 5000:
                news_content = news_content[:5000]

            # Using symbolica for summarization
            summary_query = f"Summarize the following article news_content: {news_content}"
            try:
                summary_query_symbol = Symbol(summary_query)
                summary_response = summary_query_symbol.summarize()
                summary = summary_response[0] if isinstance(summary_response, list) else summary_response
                analysis_query = f"Analyze the following news and provide an investment signal for {security_ticker}: {summary}"
                analysis_query_response = Symbol(analysis_query)
                analysis_response = analysis_query_response.summarize()
                analysis = analysis_response[0] if isinstance(analysis_response, list) else analysis_response
                investment_signal = 1 if 'buy' in analysis.lower() or 'hold' in analysis.lower() else -1
                signals.append({
                    "ticker": security_ticker,
                    "signal": investment_signal,
                    "justification": analysis,
                    "news_summary": summary
                })

            except Exception as e:
                print(f"General exception analyzing news for {security_ticker}: {e}")
                signals.append({
                    "ticker": security_ticker,
                    "signal": 0,
                    "justification": f"Exception: {str(e)}",
                    "news_summary": news_content
                })
        return signals
