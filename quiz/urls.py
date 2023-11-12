from django.urls import path
from .views import QuizListView, QuizDetailView, quiz_data_view, save_quiz_view


app_name = 'quiz'

urlpatterns = [
    path('list/', QuizListView.as_view(), name='list'),
    path('list/<slug>/', QuizDetailView.as_view(), name='detail'),
    path('list/<slug>/data/', quiz_data_view, name='quiz-data-view'),
    path('list/<slug>/save/', save_quiz_view, name='save-view')
]