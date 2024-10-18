from django import forms
from .models import Poll, Choice

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        labels = {
            'question': 'Вопрос:',  # Изменяем метку для поля вопроса
        }

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        labels = {
            'choice_text': 'Введите вариант ответа:',  # Изменяем метку для выбора текста
        }