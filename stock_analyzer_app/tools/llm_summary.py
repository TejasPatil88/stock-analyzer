import openai
import os

openai.api_key = os.getenv("openai_api_key")

def summarize_news(news_items):
    if not news_items:
        return "No recent news found."

    joined_news = "\n".join(news_items)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize recent stock news briefly."},
            {"role": "user", "content": joined_news}
        ]
    )

    return response['choices'][0]['message']['content']