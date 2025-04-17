from django.shortcuts import render,redirect
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponseServerError
from .models import Questiondb, Quizsession
import random

# def home(request):
#    return render(request,'base.html')





class QuizHomeView(TemplateView):
    template_name = 'base.html'


class StartQuizView(View):
    def get(self, request):
        return render(request, 'Quz/quize.html')


class GetQuestionView(View):
    def get(self, request, num_questions=5):
        try:
            questions = list(Questiondb.objects.all())
            if not questions:
                return render(request, 'Quz/error.html', {'error': 'No questions available'})

            random.shuffle(questions)
            selected_questions = questions[:num_questions]

            request.session['quiz_questions'] = [q.id for q in selected_questions]
            request.session.modified = True

            return render(request, 'Quz/question.html', {'questions': selected_questions})
        
        except Exception as e:
            return HttpResponseServerError(f"An error occurred: {str(e)}")


class SubmitAnswerView(View):
    def post(self, request):
        quiz_questions = request.session.get('quiz_questions', [])

        try:
            for index, question_id in enumerate(quiz_questions, start=1):
                user_answer = request.POST.get(f'answer_{index}')
                if user_answer:
                    try:
                        question = Questiondb.objects.get(id=question_id)
                        is_correct = question.right_answer == user_answer
                        Quizsession.objects.create(
                            question_id=question.id,
                            user_answer=user_answer,
                            correct=int(is_correct)
                        )
                    except Questiondb.DoesNotExist:
                        return render(request, 'Quz/error.html', {'error': 'A question was not found.'})
        except Exception as e:
            return HttpResponseServerError(f"Error during submission: {str(e)}")

        return redirect('quizengine:results')

    def get(self, request):
        return redirect('quizengine:get_question')


class ResultsView(TemplateView):
    template_name = 'Quz/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            latest_attempts = list(Quizsession.objects.order_by('-id')[:5])
            if not latest_attempts:
                return {'error': 'No quiz session found'}

            question_ids = [attempt.question_id for attempt in latest_attempts]
            quiz_attempts = Quizsession.objects.filter(question_id__in=question_ids)

            correct_count = quiz_attempts.filter(correct=True).count()
            total_questions = quiz_attempts.count()
            score = (correct_count / total_questions * 100) if total_questions > 0 else 0

            context.update({
                'quiz_attempts': quiz_attempts,
                'correct_count': correct_count,
                'incorrect_count': total_questions - correct_count,
                'total_questions': total_questions,
                'score': score
            })
        except Exception as e:
            context['error'] = f"Error calculating results: {str(e)}"
        return context


class ResetQuizView(View):
    def get(self, request):
        try:
            Quizsession.objects.all().delete()
        except Exception as e:
            return HttpResponseServerError(f"Error resetting quiz: {str(e)}")
        return redirect('quizengine:start_quiz')
