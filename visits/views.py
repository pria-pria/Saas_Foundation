from django.shortcuts import render
from .models import PageVisit


def Home(request, *args, **kwargs):
    page_title= "MY PAGE"
    queryset = PageVisit.objects.all()
    context={
        "my_title":page_title,
        "queryset":queryset.count()
    }
    PageVisit.objects.create()
    return render(request, 'home.html', context)

def about_View(request):
    context = {
        'title': 'About Us',
        'content': 'This is the about page.'
    }
    return render(request, 'about.html', context)