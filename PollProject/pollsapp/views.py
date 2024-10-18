from .forms import PollForm, ChoiceForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Choice

def index(request):
    polls = Poll.objects.all()
    return render(request, 'pollsapp/index.html', {'polls': polls})  # Измените на 'pollsapp/index.html'

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'pollsapp/detail.html', {'poll': poll})  # Измените на 'pollsapp/detail.html'

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'pollsapp/detail.html', {  # Измените на 'pollsapp/detail.html'
            'poll': poll,
            'error_message': "Выберите вариант ответа.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', poll_id=poll.id)

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'pollsapp/results.html', {'poll': poll})  # Измените на 'pollsapp/results.html'






#новое 09.09.2024

def create_poll_and_choices(request):
    if request.method == "POST":
        poll_form = PollForm(request.POST)
        choice_forms = [ChoiceForm(request.POST, prefix=str(i)) for i in range(3)]  # Предполагаем 3 варианта ответа

        if poll_form.is_valid() and all(choice_form.is_valid() for choice_form in choice_forms):
            poll = poll_form.save()
            for choice_form in choice_forms:
                choice = choice_form.save(commit=False)
                choice.poll = poll
                choice.save()
            return redirect('polls:index')  # Перенаправление на главную страницу опросов
    else:
        poll_form = PollForm()
        choice_forms = [ChoiceForm(prefix=str(i)) for i in range(3)]

    return render(request, 'pollsapp/create_poll_and_choices.html', {
        'poll_form': poll_form,
        'choice_forms': choice_forms,
    })

