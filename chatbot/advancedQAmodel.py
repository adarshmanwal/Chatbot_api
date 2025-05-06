from transformers import pipeline

class AdvancedQAModel:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering")

    def get_response(self, question, context):
        result = self.qa_pipeline(question=question, context=context)
        print("+==============================")
        print(result)
        return result['answer']
    
advancedQAmodel = AdvancedQAModel()