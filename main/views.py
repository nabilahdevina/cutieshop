from django.shortcuts import render

def show_main(request):
    context = {
        'app_store' : 'cutiemarket',
        'name': 'Nabilah Devina Mumin',
        'class': 'PBP B',
        'stock' : '30',
    }

    return render(request, "main.html", context)
