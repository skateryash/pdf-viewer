from transformers import pipeline

class QuestionAnswering:
    def __init__(self):
        self.qa = pipeline("question-answering")

    def answer_question(self, question, context):
        result = self.qa(question=question, context=context)['answer']
        return result
#
#
# qa_system = QuestionAnswering()
#
# context = "The capital of France is Paris."
# question = "What is the capital of France?"
#
# result = qa_system.answer_question(question, context)
# print(result)
