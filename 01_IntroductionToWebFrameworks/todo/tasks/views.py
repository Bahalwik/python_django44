from django.http import HttpResponse

from django.views import View
import random
random_elem = range(1, 100, 1)
class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<ul>'
                            '<li>Установить python</li>'
                            '<li>Установить django</li>'
                            '<li>Запустить сервер</li>'
                            '<li>Порадоваться результату</li>'
                            '<li>Что-то новенькое {rand}'
                            '</ul>'.format(rand=random_elem[random.randint(1, 100)]))
