from django import forms
from django.core.validators import MinValueValidator, ValidationError
from webapp.models import Type, Answer, Question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['title', 'type']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'date', 'date_end']


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')