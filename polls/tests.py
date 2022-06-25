from django.test import TestCase
from .models import Question, Choice
from django.utils import timezone
from django.test import Client

class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question_text="How old are you?", pub_date=timezone.now())

    def test_questions_count(self):
        questions_count = Question.objects.count()
        self.assertEqual(questions_count, 1)

    def test_question_text(self):
        question = Question.objects.get(question_text="How old are you?")
        self.assertEqual(str(question), "How old are you?")

    def test_question_id(self):
        question = Question.objects.get(question_text="How old are you?")
        self.assertEqual(question.id, 2)
    def test_new_question(self):
        q = Question(id=1, question_text="What's your name?", pub_date=timezone.now())
        question = Question(id=1, question_text="What's your name?", pub_date=timezone.now())
        q.save()
        question.save()

class RequestTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def setUpTestData():
        Question.objects.create(question_text="What is the capital of Russia?", pub_date=timezone.now())

    def test_get_status_code(self):
        response = self.c.get('/polls/')
        self.assertEqual(response.status_code, 200)
        print(response.content)
# Create your tests here.
