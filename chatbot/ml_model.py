from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SimpleQAModel:
    def __init__(self, qa_data):
        self.qa_data = qa_data
        self.questions = list(qa_data.keys())
        self.answers = list(qa_data.values())
        self.vectorizer = TfidfVectorizer().fit(self.questions)

    def get_response(self, query):
        query_vec = self.vectorizer.transform([query])
        question_vecs = self.vectorizer.transform(self.questions)
        similarities = cosine_similarity(query_vec, question_vecs).flatten()
        best_match_index = similarities.argmax()
        return self.answers[best_match_index]

qa_data = {
    "What model are you using to train the chatbot?": "We are using a BERT-based model fine-tuned for question answering. BERT (Bidirectional Encoder Representations from Transformers) is a powerful transformer model developed by Google.",
    "What is the motive of your model?": "The motive of our model is to accurately respond to questions related to our college project, providing clear and concise answers about the technologies, methodologies, and objectives used.",
    "Which technology are you using to achieve this?": "We are using Python, Django for the backend API, and the transformers library by Hugging Face for the AI model. Additionally, we utilize scikit-learn for basic data preprocessing.",
    "How does your chatbot work?": "The chatbot works by receiving a user question, processing it through a trained model, and then generating a response based on the training data. It leverages a BERT model to understand and answer questions.",
    "What is Django?": "Django is a high-level Python web framework that allows for rapid development of secure and maintainable websites. It handles much of the complexity of web development.",
    "Why did you choose BERT for your model?": "We chose BERT because it provides state-of-the-art performance for NLP tasks, including question answering. Its ability to understand context in both directions makes it ideal for our project.",
    "What is the objective of your chatbot?": "The objective of the chatbot is to assist users by answering questions specifically related to our college project, providing accurate information about our work, tools, and methodologies.",
    "How is the chatbot deployed?": "The chatbot is deployed using Django on a cloud-based server, allowing it to be accessed via a web interface. The model is loaded and run on the server, responding to user queries in real-time.",
    "What are the main features of your chatbot?": "The main features of our chatbot include answering project-related questions, providing detailed explanations about the tools and technologies used, and guiding users through our project's details.",
    "What challenges did you face during the project?": "Some challenges we faced include fine-tuning the model to improve accuracy, integrating the model with Django, and ensuring the chatbot could handle a wide range of questions.",
    "What datasets did you use for training?": "For training, we created a custom dataset based on the specific questions and answers related to our project. This dataset was designed to cover all the key aspects of our work.",
    "How do you evaluate the performance of your model?": "We evaluate the performance of our model using accuracy, precision, recall, and F1-score on a validation set derived from our custom dataset.",
    "What future improvements do you plan for the chatbot?": "Future improvements include expanding the dataset, optimizing the model for faster response times, and integrating additional features like sentiment analysis to enhance user interaction.",
    "What is the role of transformers in your project?": "Transformers play a crucial role in our project by enabling the chatbot to understand and generate responses to user questions. The BERT model, a type of transformer, is central to this process.",
    "Why did you choose Django for your project?": "We chose Django because it is a robust and scalable web framework that simplifies the process of building and deploying web applications. Its built-in features and security make it ideal for our needs.",
    "What is the significance of fine-tuning in your project?": "Fine-tuning is significant because it allows us to adapt a pre-trained BERT model to our specific dataset, improving its performance in answering project-related questions accurately."
}


model = SimpleQAModel(qa_data)
