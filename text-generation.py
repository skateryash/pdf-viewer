from transformers import pipeline


class TextGenerator:
    def __init__(self):
        self.generator = pipeline("text-generation")

    def generate_text(self, prompt, max_length=50, do_sample=False):
        generated_text = self.generator(prompt, max_length=max_length, do_sample=do_sample)
        return generated_text


generator_system = TextGenerator()

prompt = "Once upon a time"
generated_text = generator_system.generate_text(prompt)
print(generated_text)

