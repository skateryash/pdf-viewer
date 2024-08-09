from transformers import pipeline


class NamedEntityRecognition:
    def __init__(self):
        self.ner = pipeline("ner")

    def recognize_entities(self, text):
        result = self.ner(text)
        ner_list = {}
        for item in result:
            word = item["word"]
            entity = item['entity']
            ner_list[word] = entity
        return ner_list
