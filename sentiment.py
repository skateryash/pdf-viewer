from transformers import pipeline


class SentimentAnalyzer:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis")

    def analyze_sentiment(self, text):
        result = self.classifier(text)
        return result


# sentiment_analyzer = SentimentAnalyzer()
# text = "I love this movie!"
# result = sentiment_analyzer.analyze_sentiment(text)
# label = result[0]['label']
# score = result[0]['score']*100
# print(f"Sentiment: {label}\nAccuracy: {score:.2f}%")
