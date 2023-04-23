from django.shortcuts import render
from .models import News, Games


def index(request):
    news = News.objects.all().order_by('-id').prefetch_related('photos')
    games = Games.objects.all()

    print(games)

    context = {
        'news': news,
    }

    return render(request, 'index.html', context)
