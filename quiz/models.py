from django.template.defaultfilters import slugify 
from django.db import models
from django.contrib.auth.models import User
import random
import datetime

DIFF_CHOICSES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):
    name                    = models.CharField(max_length=120)
    topic                   = models.CharField(max_length=120)
    slug                    = models.SlugField()
    number_of_questions     = models.IntegerField()
    time                    = models.IntegerField(help_text='duration of the quiz in minutes')
    required_score_to_pass  = models.IntegerField(help_text='required score in %')
    difficulty              = models.CharField(max_length=6, choices=DIFF_CHOICSES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'

class Question(models.Model):
    text = models.CharField(max_length=225)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text        = models.CharField(max_length=225)
    correct     = models.BooleanField(default=False)
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    created     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

class Result(models.Model):
    quiz    = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    score   = models.FloatField()
    created = models.DateField(auto_now_add=True) #true =  now when first created
    updated = models.DateField(auto_now=True) # set the field to now every time the object is saved. Useful for “last-modified” timestamp
    expired = models.DateField()

    def __str__(self):
        return f"{self.user} scored: {self.score}% on{self.quiz}.\n It was created on {self.created}, \n It was updated on {self.updated},  \n It expires on {self.expired}"
    
    def passed(self):
        if self.score >= self.quiz.required_score_to_pass:
            return f'Congratulations. You have passed {self.quiz.name}'
        return f'Please try again.You have not passed {self.quiz.name}, '
