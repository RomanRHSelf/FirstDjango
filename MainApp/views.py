from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item, Color
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

#items = [
#{"id": 1, "name": "Кроссовки aдiдas" ,"quantity":5},
#{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#{"id": 7, "name": "Картофель фри" ,"quantity":0},
#{"id": 8, "name": "Кепка" ,"quantity":124},
#]

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
    <header>
        / <a href="/"> Начальная страница </a> / <a href="/items/"> Список товаров </a> / <a href="/about/"> О сайте (из процедуры)</a>
    </header>
    <h1>Об авторе</h1>
    <strong>Имя</strong>: <i>Иван</i> <br>
    <strong>Отчество</strong>: <i>Петрович</i> <br>
    <strong>Фамилия</strong>: <i>Иванов</i> <br>
    <strong>телефон</strong>: <i>8-923-600-01-02</i> <br>
    <strong>email</strong>: <i>vasya@mail.ru</i>
    <br><br>
    не шаблон - просто текст из процедуры about в httpResponse
    """
    return HttpResponse(text)
          
def get_item(request, item_id:int):
    try:
        item_from_db = Item.objects.get(id=item_id)
        item_clrs = item_from_db.colors.all() #Color.objects.all(id=item_id)
        context = {
            "Main_head": "template for item",
            "item_id": item_from_db.id,
            "name": item_from_db.name,
            "brand": item_from_db.brand,
            "quantity": item_from_db.count,
            "description": item_from_db.description,
            "item_colors": item_clrs
        }
        return render(request=request, template_name="item_from_db.html", context=context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Товар {item_id} не найден')

def get_items(request):
    items_from_db = Item.objects.all()
    context = {
        "items_list": items_from_db,
        "Main_head" : "все товары",
    }
    return render(request=request, template_name="items_list_from_db.html", context=context)