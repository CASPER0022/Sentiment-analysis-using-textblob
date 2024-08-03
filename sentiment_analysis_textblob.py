from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"

user_input = input("Enter your text: ")
result = analyze_sentiment(user_input)
print(f"The sentiment of your text is: {result}")