from django.shortcuts import get_object_or_404, redirect
from webapp.models import Answer, Question
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.forms import AnswerForm


class IndexView(ListView):
    template_name = 'answers/answer_index.html'
    model = Answer
    context_object_name = 'answers'
    ordering = ('title', '-created_ad')
    paginate_by = 10
    paginate_orphans = 3


class AnswerView(DetailView):
    template_name = 'answers/answer_view.html'
    model = Answer
    context_object_name = 'answer'


class CreateAnswerView(CreateView):
    template_name = 'answers/answer_create.html'
    model = Answer
    form_class = AnswerForm

    def form_valid(self, form):
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        answer = form.save(commit=False)
        answer.answer = question
        answer.save()
        return redirect('answer-view', pk=answer.pk)

    def get_success_url(self):
        return reverse('answer-view', kwargs={'pk': self.object.pk})


class AnswerUpdateView(UpdateView):
    model = Answer
    template_name = 'answers/answer_update.html'
    form_class = AnswerForm
    context_object_name = 'answer'

    def get_success_url(self):
        return reverse('answer-view', kwargs={'pk': self.object.pk})


class AnswerDeleteView(DeleteView):
    template_name = 'answers/answer_delete.html'
    model = Answer
    context_object_name = 'answer'

    success_url = reverse_lazy('answer-list')







