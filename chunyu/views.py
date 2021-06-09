from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, '../templates/index.html', context=context)


def generic(request):
    return render(request, '../templates/generic.html', locals())


def elements(request):
    return render(request, '../templates/elements.html', locals())