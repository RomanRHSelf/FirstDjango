from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

item_s = [
{"id": 1, "name": "Кроссовки aдiдas" ,"quantity":5},
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
    context = {
        "Main_title": "Заглавная страница",
        "name": "Вася Васьевич Васькин",
        "email": "Vasin_mail@mail.com"
    }
    return render(request=request, template_name="index.html", context=context) #HttpResponse(text)

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

def get_item(request, item_id:int):
    text = None
    for item in item_s:
        if item["id"] == item_id:            
            text = f"""
            <h1>{item_id=}</h1>
            <h2>Наименование: <i>{item['name']}</i> </h2>
            <p>Количество: <i>{item['quantity']}</i> </p> <br>
            <p><a href="/items"> Вернуться к полному списку товаров </a></p>
            """
            return HttpResponse(text)
    return HttpResponse(f"Товар {item_id=} не найден" if text is None else text) # HttpResponseNotFound(f'Товар {item_id=} не найден')
       
def get_item_1(request):
    text = None
    for item in item_s:
        if item["id"] == 1:
            text = f"""
            <h1>Специально и только для item_id=1</h1>
            <h2>Наименование: <i>{item['name']}</i> </h2>
            <p>Количество: <i>{item['quantity']}</i> </p> <br>
            <p><a href="/items"> Вернуться к полному списку товаров </a></p>
            """
            # return HttpResponse(text)
    context = {
        "Main_head": "Special for item 1",
        "text_html": text
    }
    # return HttpResponseNotFound(f'Товар id=1 не найден')
    return render(request=request, template_name="item.html", context=context)

def get_items(request):
    text = """<h1> Список всех товаров: </h1>
              <ol>"""
    for item in item_s:
        text += f'''<li> 
                    <b>{item["id"]}: </b> 
                    <a href="/item/{item["id"]}" > {item["name"]} </a> 
                    </li>'''
    text += "</ol>"
    return HttpResponse(text)

def get_items_template(request):
    text = """<h1> Список всех товаров: </h1>
              <ol>"""
    for item in item_s:
        text += f'''<li> 
                    <b>{item["id"]}: </b> 
                    <a href="/item/{item["id"]}" > {item["name"]} </a> 
                    </li>'''
    text += "</ol>"
    return HttpResponse(text)