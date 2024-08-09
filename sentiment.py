from transformers import pipeline


class SentimentAnalyzer:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis")

    def analyze_sentiment(self, text):
        result = self.classifier(text)
        return result
