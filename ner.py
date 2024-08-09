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


# ner_system = NamedEntityRecognition()
# result = ''
# text = "Apple is a company based in California."
# ner_list = ner_system.recognize_entities(text)
# print(ner_list)
#
# for key, value in ner_list.items():
#     # print(f"{key}: {value}")
#     result = result + f"{key}: {value}" + "\n"
#
# print(result)


# # print(len(result))
# # [{'entity': 'I-ORG', 'score': 0.9978593, 'index': 1, 'word': 'Apple', 'start': 0, 'end': 5},
# #  {'entity': 'I-LOC', 'score': 0.9993625, 'index': 7, 'word': 'California', 'start': 28, 'end': 38}]


