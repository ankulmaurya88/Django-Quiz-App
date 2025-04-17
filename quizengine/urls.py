
from django.contrib import admin
from django.urls import path,include
from . import views 
app_name = "quizengine" 

# urlpatterns = [
# path("",views.home, name="home"),
# ]


from django.urls import path
from .views import (
    QuizHomeView, StartQuizView, GetQuestionView,
    SubmitAnswerView, ResultsView, ResetQuizView
)

app_name = 'quizengine'

urlpatterns = [
    path('', QuizHomeView.as_view(), name='home'),
    path('start/', StartQuizView.as_view(), name='start_quiz'),
    path('questions/', GetQuestionView.as_view(), name='get_question'),
    path('submit/', SubmitAnswerView.as_view(), name='submit_answer'),
    path('results/', ResultsView.as_view(), name='results'),
    path('reset/', ResetQuizView.as_view(), name='reset_quiz'),
]
