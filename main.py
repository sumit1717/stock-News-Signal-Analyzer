from config import SYMBOLIC_AI_ENGINE
from news_retriever import NewsRetriever
from news_analyzer import NewsAnalyzer
from result_saver import ResultSaver
from utils import get_security_tickers
from symai import *

# from symai.backend.engine_gptX_chat import GPTXChatEngine
#
# custom_engine = GPTXChatEngine()
# custom_engine.model = SYMBOLIC_AI_ENGINE


def main():
    # Expression.setup(engines={'neurosymbolic': custom_engine})

    securities = get_security_tickers()
    news_retriever = NewsRetriever()
    news_analyzer = NewsAnalyzer()
    result_saver = ResultSaver()

    all_signals = []

    for ticker in securities:
        news_articles = news_retriever.fetch_news(ticker)
        if not news_articles:
            print(f"No news found for {ticker}")
            continue
        signals = news_analyzer.evaluate_news(ticker, news_articles, news_retriever)
        all_signals.extend(signals)
        result_saver.save_to_json(ticker, news_articles)

    result_saver.save_to_excel(all_signals)


if __name__ == "__main__":
    main()
