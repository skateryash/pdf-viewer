from transformers import pipeline


class TextSummarizer:
    def __init__(self):
        self.summarizer = pipeline('summarization')

    def summarize_text(self, text):
        summary = self.summarizer(text)[0]['summary_text']
        return summary
