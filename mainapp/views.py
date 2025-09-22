from django.shortcuts import render

def index(request):
    title = 'Главная'

    context = {
        'title': title,
    }
    return render(request, 'index.html', context)


def contacts(request):
    title = 'Контакты hajagan kajaradagan'

    context = {
        'title': title,
    }
    return render(request, 'contacts.html', context)


def productone(request):
    title = 'Продукт'

    context = {
        'title': title,
    }
    return render(request, 'productone.html', context)


def products(request):
    title = 'Продукты'

    context = {
        'title': title,
    }
    return render(request, 'products.html', context)


def about(request):
    title = 'О нас'

    context = {
        'title': title,
    }
    return render(request, 'products.html', context)

