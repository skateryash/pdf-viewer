# # pip install googletrans
# # pip install deep-translator
import googletrans
from deep_translator import GoogleTranslator


class TextTranslator:
    def __init__(self):
        self.langdict = googletrans.LANGUAGES

    def translate_text(self, text, target_language):
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated_text


# Testing code
# translator = TextTranslator()
# target_language = "hi"  # Change this to your desired target language code
# doc = """
# # Usually any machine learning or deep learning process has some similar steps, but in this case of terms of flow it is so simple any typical machine learning life Lord any process has some of the steps like collection of data set than building the model training the network evaluating the model and then predicting the outcome in case of tensorflow.Tensorflow bundles together a study of machine learning and deep learning models and algorithms and make them useful by way of common metaphor who will use machine learning and all of its products to improve the search engine the translation image captioning or the recommendations to give you a concrete example, Google users can experience a faster and more refined search with artificial intelligence.Each node in the graph represents a mathematical operation and each connection or Edge between the notes is a multi-dimensional data array or tensile test flow provides all of this for the programmer by way of the Python language by then is easy to learn and work with and provides convenient ways to express how high-level abstraction can be coupled together notes and the tensor in the tensorflow our python objects.China mobile is using tensorflow to improve their success rate of the network element cut overs Channel while has created a deep Fist amusing tensorflow that can automatically predicts the cut over time window verify log operations and detect Network anomalies and this has already successfully supported the world's largest relocation of hundreds of millions iot HSS.is training a neural network to identify specific anatomic during the brain MRI exam to help improve speed and reliability now PayPal is using it as a flow to stay at The Cutting Edge of fraud detection using tensorflow deep trance for Learning and Generator modeling PayPalCNTK the Microsoft cognitive toolkit, like tensorflow uses a graph structure to describe the data flow, but it focuses more on creating deep learningIt is also in the market another thing that gives tensorflow Edge over other competitors is the fact that it is open source and has a huge Community Support that not only provides researchers a way to build new models, but also a platform to interact with others that face some issues if we talk about a simple program in terms of flow.Thanks to machine learning Frameworks such as Google's TensorFlow that ease the process of acquiring data, training model, solving predictions and refining future results.The Airbnb ingenious and data science team applies machine learning using tensorflow to classify the images and detect objects at scale helping to improve the guest experienceYou can build and train models by using the high-level Kira's API, which makes getting started with tensorflow and machine learning very very easy.Now the actual math operations however are not performed in Python the libraries of transformation data available through tears flow are written as high performance C++ binaries python just directs the traffic between the pieces and provides high level programming attraction to hook them together now building a new rail.Machine learning is a complex discipline but implementing machine learning models is far less daunting and difficult than it used to be.There's a flow allows the developers to create a data flow graphs which are structures that describe how the data move through a graph or a series of processing nodes.Created by the Google brain team tensorflow is an open source library for numerical computation and large scale machine learning.The model is also a single line of code now training a neural network cannot get any more easier than this and that is why it is the flow remains at the top when compared to the other competitors.No talking about Apache MXNet adopted by Amazon as a premier deep learning framework on AWS can scale almost linearly across multiple gpus and multiple machine.If you need more flexibility Iker execution allows for immediate iteration and intuitive debugging when you enable eager execution, you will be executing tensorflow kernels immediately rather than constructing graphs that will be executed laterThe network is just a single line evaluating the network or the model itself is a single line of code and predicting.
# # """
# translated_text = translator.translate_text(doc, target_language)
# print("YOUR TRANSLATED SUMMARY IS GIVEN BELOW:")
# print(" ")
# print(translated_text)


