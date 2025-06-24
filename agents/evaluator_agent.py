

import google.generativeai as genai
from django.conf import settings

# Gemini API configure
genai.configure(api_key=settings.GEMINI_API_KEY)

class AnswerEvaluatorAgent:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def run(self, user_answer, correct_answer):
        prompt = f"""
        Student answered: "{user_answer}".
        The correct answer is: "{correct_answer}".
        Tell if it's 'Correct', 'Incorrect', or 'Incomplete'.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error: {str(e)}"
