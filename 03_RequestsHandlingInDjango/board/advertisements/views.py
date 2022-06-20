from django.shortcuts import render, redirect
from .forms import TaskForm

def home(request):
    return render(request, 'advertisements/home.html', {})


def advertisement_list(request):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    advertisements_1 = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]

    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                      'advertisements_1': advertisements_1})


def create_advertisement(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка в форме'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'advertisements/create_advertisement.html', context)


def contacts(request):
    return render(request, 'advertisements/contacts.html', {})


def about(request):
    return render(request, 'advertisements/about.html', {})

