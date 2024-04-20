from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
# Create your views here.

items = [
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
    for item in items:
        if item["id"] == item_id:            
            text = f"""
            <h1>{item_id=}</h1>
            <h2>Наименование: <i>{item['name']}</i> </h2>
            <p>Количество: <i>{' товар отсутствует' if item['quantity'] == 0 else item['quantity']}</i> </p> <br>
            <p><a href="/items"> Вернуться к полному списку товаров </a></p>
            """
            return HttpResponse(text)
    return HttpResponse(f"Товар {item_id=} не найден" if text is None else text) # HttpResponseNotFound(f'Товар {item_id=} не найден')
       
def get_item_template(request, item_id:int):
    for item in items:
        item_id_lockal = item["id"]
        if item["id"] == item_id:
            context = {
                "Main_head": "tamplate for item",
                "item_id": item_id_lockal,
                "name": item['name'],
                "quantity": item['quantity'],
            }
            return render(request=request, template_name="item.html", context=context)
    return HttpResponseNotFound(f'Товар {item_id} не найден')
    
def get_item_from_db(request, item_id:int):
    items_from_db = Item.objects.all()
    for item in items_from_db:
        item_id_lockal = item.id
        if item.id == item_id:
            context = {
                "Main_head": "tamplate for item",
                "item_id": item_id_lockal,
                "name": item.name,
                "brand": item.brand,
                "quantity": item.count,
            }
            return render(request=request, template_name="item_from_db.html", context=context)
    return HttpResponseNotFound(f'Товар {item_id} не найден')

def get_items(request):
    text = """<h1> Список всех товаров: </h1>
              <ol>"""
    for item in items:
        text += f'''<li> 
                    <b>{item["id"]}: </b> 
                    <a href="/item/{item["id"]}" > {item["name"]}, кол-во: {item["quantity"]}</a> 
                    </li>'''
    text += "</ol>"
    return HttpResponse(text)

def get_items_template(request):
    context = {
        "items_list": items,
        "Main_head" : "все товары",
    }
    return render(request=request, template_name="items.html", context=context)

def get_items_list_from_db(request):
    items_from_db = Item.objects.all()
    context = {
        "items_list": items_from_db,
        "Main_head" : "все товары",
    }
    return render(request=request, template_name="items_list_from_db.html", context=context)