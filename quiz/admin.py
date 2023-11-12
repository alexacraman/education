from unittest import result
from django.contrib import admin

from .models import Result, Quiz, Question, Answer


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'number_of_questions', 'required_score_to_pass')
    prepopulated_fields ={'slug': ('name',)}

admin.site.register(Quiz, QuizAdmin)

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'user', 'score', 'created', 'updated', 'expired')

admin.site.register(Result, ResultAdmin)