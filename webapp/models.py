from audioop import reverse

from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=3000, null=False, blank=False)

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class Answer(BaseModel):
    title = models.CharField(max_length=3000, null=False, blank=False)
    answer = models.ForeignKey('webapp.Question', null=True, related_name="question_answer", default=1,
                                on_delete=models.CASCADE)

    class Meta:
        db_table = 'Answers'
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'


class Question(BaseModel):
    title = models.CharField(max_length=200, null=False, blank=False)


    class Meta:
        db_table = 'Questions'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

