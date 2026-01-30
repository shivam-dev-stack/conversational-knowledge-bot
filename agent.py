from transformers import pipeline
from ddgs import DDGS

class KnowledgeBot:

    def __init__(self):

        # Question Answering model (CPU friendly)
        self.qa = pipeline(
            "question-answering",
            model="deepset/roberta-base-squad2"
        )

        self.search = DDGS()
        self.history = []

    def ask(self, question):

        if self.history:
            full_question = f"{self.history[-1]} {question}"
        else:
            full_question = question

        self.history.append(full_question)

        results = list(self.search.text(full_question, max_results=5))

        if not results:
            return "No search results found."

        context = " ".join([r["body"] for r in results])

        answer = self.qa(
            question=question,
            context=context
        )

        return answer["answer"]
