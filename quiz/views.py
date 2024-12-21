from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Question, QuizSession
from django.db.models import Count

def start_quiz(request):
    return render(request, 'quiz/base.html')

def get_question(request):
    question = Question.objects.order_by('?').first()
    return render(request, 'quiz/question.html', {'question': question})

def submit_answer(request):
    if request.method == 'POST':
        question_id = request.POST['question_id']
        user_answer = request.POST['answer']
        question = Question.objects.get(id=question_id)

        is_correct = question.correct_option == user_answer
        QuizSession.objects.create(question=question, user_answer=user_answer, correct=is_correct)

        return redirect('quiz:results')

def results(request):
    sessions = QuizSession.objects.all()
    correct_count = sessions.filter(correct=True).count()
    incorrect_count = sessions.filter(correct=False).count()
    return render(request, 'quiz/results.html', {
        'sessions': sessions,
        'correct_count': correct_count,
        'incorrect_count': incorrect_count
    })


def reset_quiz(request):
    QuizSession.objects.all().delete()
    return render(request, 'quiz/base.html')