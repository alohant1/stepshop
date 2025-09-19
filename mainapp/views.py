from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


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

