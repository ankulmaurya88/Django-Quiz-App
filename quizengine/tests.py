from django.test import TestCase, Client
from django.urls import reverse
from .models import Quiz, Question  # Replace with your actual models

class QuizEngineModelTest(TestCase):
    def setUp(self):
        self.quiz = Quiz.objects.create(title="Sample Quiz")
        self.question = Question.objects.create(
            quiz=self.quiz, text="What is 2 + 2?", answer="4"
        )

    def test_quiz_creation(self):
        self.assertEqual(self.quiz.title, "Sample Quiz")

    def test_question_creation(self):
        self.assertEqual(self.question.text, "What is 2 + 2?")
        self.assertEqual(self.question.answer, "4")


class QuizEngineViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_quiz_list_page(self):
        response = self.client.get(reverse("quiz-list"))  # Replace "quiz-list" with your URL name
        self.assertEqual(response.status_code, 200)

    def test_quiz_detail_page(self):
        # Create a quiz to test
        from .models import Quiz
        quiz = Quiz.objects.create(title="Detail Quiz")
        response = self.client.get(reverse("quiz-detail", args=[quiz.id]))  # Replace URL name
        self.assertEqual(response.status_code, 200)
