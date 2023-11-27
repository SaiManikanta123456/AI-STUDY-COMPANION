import requests
api_key="9171f8958ba34bdd9bbece446d13c9ef"


def news(language='en'):  # Change the language here, 'es' for Spanish
    main_url = f"https://newsapi.org/v2/top-headlines?country=in&category=politics&apiKey={api_key}&language={language}"
    news = requests.get(main_url).json()
    articles = news["articles"]

    news_articles = [article['title'] for article in articles]

    for i in range(3):
        print(news_articles[i])
news()


# 9171f8958ba34bdd9bbece446d13c9ef