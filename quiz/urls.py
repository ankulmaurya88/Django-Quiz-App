from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.start_quiz, name='start'),
    path('question/', views.get_question, name='question'),
    path('submit/', views.submit_answer, name='submit'),
    path('results/', views.results, name='results'),
    path('reset/', views.reset_quiz, name='reset')
]
