import yfinance as yf
from tools.news_scraper import get_latest_news
from tools.llm_summary import summarize_news

def get_stock_ticker(query):
    # Simple validation, can be extended with actual mapping
    if "." not in query:
        raise ValueError("Please enter a valid ticker (e.g., RELIANCE.NS or TCS.BO)")
    return query.upper(), query.upper()

def Anazlyze_stock(query):
    company_name, ticker = get_stock_ticker(query)
    stock = yf.Ticker(ticker)

    info = stock.info
    if not info:
        raise ValueError("No data found for this ticker.")

    summary_html = f'''
    <h2>{info.get("longName", ticker)}</h2>
    <ul>
        <li><strong>Sector:</strong> {info.get("sector", "N/A")}</li>
        <li><strong>Market Cap:</strong> {info.get("marketCap", "N/A")}</li>
        <li><strong>52W High:</strong> {info.get("fiftyTwoWeekHigh", "N/A")}</li>
        <li><strong>52W Low:</strong> {info.get("fiftyTwoWeekLow", "N/A")}</li>
        <li><strong>PE Ratio:</strong> {info.get("trailingPE", "N/A")}</li>
        <li><strong>Dividend Yield:</strong> {info.get("dividendYield", "N/A")}</li>
    </ul>
    '''

    news = get_latest_news(info.get("longName", ticker))
    summary = summarize_news(news)

    return summary_html + "<hr><h3>📄 News Summary</h3>" + summary