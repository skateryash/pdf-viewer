# **PDF Processing and NLP Toolkit**

## **Table of Contents**
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Contributing](#contributing)

## **Project Overview**

This project is a PDF processing and Natural Language Processing (NLP) toolkit designed to enhance the functionality of PDF readers by integrating various NLP capabilities. It allows users to perform tasks such as sentiment analysis, text generation, translation, summarization, question answering, named entity recognition, and text-to-speech on the content of PDF files.

## **Features**

- **PDF Navigation**: Browse through PDF files, navigate between pages, and perform custom searches.
- **Text Analysis**:
  - **Sentiment Analysis**: Analyze the sentiment of the text within a PDF.
  - **Text Generation**: Generate new text based on a given prompt.
  - **Translation**: Translate the content of the PDF into different languages.
  - **Summarization**: Summarize the content of a PDF.
  - **Question Answering**: Ask questions based on the content of the PDF and receive answers.
  - **Named Entity Recognition (NER)**: Identify and classify entities in the text (e.g., names of people, organizations, locations).
  - **Text-to-Speech**: Convert text content into spoken words.
- **User Interaction**: Customizable search options, page zoom, day/night modes, and more.

## **Installation**

To get started with the project, follow the instructions below:

### **Prerequisites**
- Python 3.7 or higher
- Required Python libraries: `transformers`, `pyttsx3`, `googletrans`, `deep_translator`, `PySimpleGUI`

### **Clone the Repository**

```bash
git clone https://github.com/skateryash/pdf-viewer.git
cd pdf-viewer
```

### **Install Dependencies**

```bash
pip install -r requirements.txt
```

## **Usage**

After installing the dependencies, you can run the application by executing the main script:

```bash
python pdfviewer.py
```

### **Key Bindings and Commands**
- **Open a PDF File**: Click on the "Open File" button or use the keyboard shortcut.
- **Navigate Pages**: Use the arrow keys or the navigation buttons.
- **Perform NLP Tasks**: Use the buttons provided for tasks such as translation, summarization, sentiment analysis, etc.

## **Modules**

### **SentimentAnalyzer**
Analyzes the sentiment of the text using a pre-trained model from the Hugging Face `transformers` library.

### **TextGenerator**
Generates text based on a given prompt using a pre-trained text generation model.

### **TextTranslator**
Translates text into a specified target language using Google Translate API.

### **NamedEntityRecognition**
Performs Named Entity Recognition to identify entities in the text.

### **TextSummarizer**
Summarizes the text content using a summarization model.

### **Text-to-Speech**
Converts text to speech using the `pyttsx3` library.

### **Event Handling**
Handles user inputs and interactions, such as navigation, search, and NLP task execution.

## **Contributing**

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
