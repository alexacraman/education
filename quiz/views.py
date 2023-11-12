from django.shortcuts import get_object_or_404
from .models import Answer, Quiz, Question, Result
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
import json
import datetime

class QuizListView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    template_name = 'quiz/list.html'
    model = Quiz


class QuizDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    template_name = 'quiz/detail.html'
    model = Quiz

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Quiz, slug=slug)

def quiz_data_view(request, slug):
    quiz = Quiz.objects.get(slug=slug)
    questions = []
    for q in quiz.get_questions():
        answers =[]
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def save_quiz_view(request, slug):
    body = json.loads(request.body)
    questions = []
    # data = body['data']
    # print(body)
    # print(type(body))
    for k in body.keys():
        question = Question.objects.get(text=k)
        # print('key: ', k)
        questions.append(question)
    # print(questions)
    user = request.user
    quiz = Quiz.objects.get(slug=slug)
    score = 0
    multiplier = 100 / quiz.number_of_questions
    results = []
    correct_answer = None

    for q in questions:
        a_selected = body[q.text]
        # print("q.text: " , a_selected)
        if a_selected != "":
            question_answers = Answer.objects.filter(question=q)
            # print(question_answers)
            for a in question_answers:
                # print("a", a)
                if a_selected == a.text:
                    # print('a_selected ', a_selected, "a.text ", a.text)
                    if a.correct:
                        score += 1
                        correct_answer = a.text
                else:
                    if a.correct:
                        correct_answer = a.text

            results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
        else:
            results.append({str(q): 'not answered'})
        
    score_ = score * multiplier


    one_year_from_now = datetime.date.today() + datetime.timedelta(365)
    try:
        obj = Result.objects.get(quiz=quiz, user=user)
        obj.quiz =quiz
        obj.user =user
        obj.score = score_
        # obj.updated = datetime.date.today() 
        obj.expired = one_year_from_now
        obj.save()
        print('upated obj:', obj)
    except Result.DoesNotExist:
        obj = Result.objects.create(quiz=quiz, user=user, score=score_, expired=one_year_from_now)
        print('Uncreated obj:', obj)

    if score_ >= quiz.required_score_to_pass:
        return JsonResponse({'passed': True, 'score': score_, 'results': results})
    else:

        return JsonResponse({'passed': False, 'score': score_, 'results': results})









    # defaults = {'score': score_}
    # try:
    #     obj = Result.objects.get(quiz=quiz, user=user)
    #     for key, value in defaults.items():
    #         setattr(obj, key, value)
    #     obj.save()
    # except Result.DoesNotExist:
    #     new_values = {'quiz':quiz, 'user':user}
    #     new_values.update(defaults)
    #     obj = Result(**new_values)
    #     obj.save()
    # try:
    #     obj = Result.objects.update(quiz=quiz, user=user, score=score_)
    # except Result.DoesNotExist:
    #     obj  = Result.objects.create(quiz=quiz, user=user, score=score_)   
    # obj = Result(quiz=quiz, user=user, score=score_)
    # obj.save()

    
    # obj = Result.objects.get(quiz=quiz, user=user, score=score_)
    # if obj is not None:
    #     obj.delete()
    #     new_obj = Result(quiz=quiz, user=user, score=score_)
    #     new_obj.save()

    # try:
    #     obj = Result.objects.get(quiz=quiz, user=user, score=score_)
    #     if obj is not None:
    #         obj.delete()
    # except Result.DoesNotExist:
    #     obj = Result.objects.create(quiz=quiz, user=user, score=score_)

    # obj = Result.objects.get(quiz=quiz, user=user)
    # print(obj)
    # update_obj = Result.objects.create(quiz=quiz, user=user, score=score_)
    # obj = update_obj
    # print(obj)
    # obj.save()