import symai as ai
from symai import *
from config import SYMBOLIC_AI_ENGINE, OPENAI_API_KEY


class NewsAnalyzer:
    def __init__(self):
        self.engine = ai.Engine()

    def evaluate_news(self, security_ticker, news_articles, retriever):
        signals = []
        for article in news_articles:
            url = article.get('link')
            if not url:
                continue
            news_content = retriever.fetch_article_content(url)
            if not news_content:
                continue

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
