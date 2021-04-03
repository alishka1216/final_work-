from django.contrib import admin
from django.urls import path
from webapp.views import (
    IndexView,
    CreateAnswerView,
    AnswerView,
    AnswerUpdateView,
    AnswerDeleteView,
    QuestionList,
    QuestionView,
    QuestionCreate,
    QuestionDelete,
    QuestionUpdate,
)

# question = project
# answer = tracker


urlpatterns = [
    path('admin/', admin.site.urls),
    path('answer/', IndexView.as_view(), name='answer-list'),
    path('answer/add/<int:pk>/', CreateAnswerView.as_view(), name='answer-add'),
    path('answer/<int:pk>/', AnswerView.as_view(), name='answer-view'),
    path('answer/update/<int:pk>/', AnswerUpdateView.as_view(), name='answer-update'),
    path('answer/delete/<int:pk>/', AnswerDeleteView.as_view(), name='answer-delete'),
    path('', QuestionList.as_view(), name='question-list'),
    path('question/<int:pk>/', QuestionView.as_view(), name='question-view'),
    path('question/add/', QuestionCreate.as_view(), name='question-add'),
    path('question/update/<int:pk>/', QuestionUpdate.as_view(), name='question-update'),
    path('question/delete/<int:pk>/', QuestionDelete.as_view(), name='question-delete'),
    ]
