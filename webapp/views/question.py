from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Question, Answer
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import AnswerForm, SearchForm, QuestionForm



class QuestionList(ListView):
    template_name = 'questions/question_index.html'
    model = Question
    context_object_name = 'questions'
    ordering = ('title',)
    paginate_by = 10
    paginate_orphans = 3


class QuestionView(DetailView):
    template_name = 'questions/question_view.html'
    model = Question
    context_object_name = 'question'


class QuestionCreate(CreateView):
    template_name = 'questions/question_create.html'
    model = Question
    form_class = QuestionForm

    def get_success_url(self):
        return reverse('question-view', kwargs={'pk': self.object.pk})


class QuestionUpdate(UpdateView):
    model = Question
    template_name = 'questions/project_update.html'
    form_class = QuestionForm
    context_object_name = 'question'


class QuestionDelete(DeleteView):
    template_name = 'questions/project_delete.html'
    model = Question
    context_object_name = 'question'

    success_url = reverse_lazy('question-list')