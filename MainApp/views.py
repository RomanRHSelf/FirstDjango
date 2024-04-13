from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

item_s = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    #text = """
    #<h1>"Изучаем django"</h1>
    #<strong>Автор</strong>: <i>Иванов И.П.</i>
    #"""
    return render(request, "index.html") #HttpResponse(text)

def about(request):
    text = """
    <h1>Об авторе</h1>
    <strong>Имя</strong>: <i>Иван</i> <br>
    <strong>Отчество</strong>: <i>Петрович</i> <br>
    <strong>Фамилия</strong>: <i>Иванов</i> <br>
    <strong>телефон</strong>: <i>8-923-600-01-02</i> <br>
    <strong>email</strong>: <i>vasya@mail.ru</i>
    """
    return HttpResponse(text)

def item(request, item_id:int):
    text = None
    for t in item_s:
        if t["id"] == item_id:
            #text = "item_id: " + str(item_id) + ", Наименование: " + str(t['name']) + ", Количество: " + str(t['quantity'])
            text = f"<h1>{item_id=}</h1> \
                     <strong>Наименование</strong>: <i>{t['name']}</i> <br> \
                     <strong>Количество</strong>: <i>{t['quantity']}</i>"
            return HttpResponse(f"item_id: {str(item_id)} не найден" if text is None else text)

def items(request):
    #<ol>
    #   <li> ... </li>
    #   <li> ... </li>
    #   <li> ... </li>
    #</ol>
    text = "<h1> Список товаров </h1><ol>"    

    return HttpResponse(text)