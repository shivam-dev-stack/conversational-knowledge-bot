from transformers import pipeline
from ddgs import DDGS

"""
Conversational Knowledge Bot using DuckDuckGo + RoBERTa QA
with simple entity memory for follow-ups.
"""

class KnowledgeBot:

    def __init__(self):

        self.qa = pipeline(
            "question-answering",
            model="deepset/roberta-base-squad2"
        )

        self.search = DDGS()
        self.last_entity = None

    def ask(self, question):

        q = question.lower().strip()

        # Follow-up detection
        if self.last_entity and q.startswith(("where", "when", "what", "who")):
            search_query = f"{self.last_entity} {question}"
            qa_question = f"{question} ({self.last_entity})"
        else:
            search_query = question
            qa_question = question

        results = list(self.search.text(search_query, max_results=5))

        if not results:
            return "No search results found."

        context = " ".join([r["body"] for r in results])

        answer = self.qa(
            question=qa_question,
            context=context
        )["answer"]

        if not answer:
            return "Sorry — I couldn't extract a clean answer."

        answer = answer.strip()

        if len(answer.split()) <= 1:
            return "Sorry — answer too short. Please try again."

        # Only store entity on WHO questions
        if question.lower().startswith("who"):
            self.last_entity = answer

        return answer
