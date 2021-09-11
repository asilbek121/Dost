from django.shortcuts import render
from main.models import *
# Create your views here.
def index(request):
    main = Hero_S.objects.all()
    azo = Counts_S.objects.all()
    Features = Features_S.objects.all()
    info = About_S.objects.all()
    reques = Questions_S.objects.all()
    data = {
        'hero': main,
        'info': info,
        'azo': azo,
        'Features': Features,
        'request ': reques,

    }
    return render(request, 'main/index.html', {'data': data})
def contact(request):
    return render(request, 'main/contact.html')
def portfolio(request):
    return render(request, 'main/portfolio.html')
def about(request):
    info = About_S.objects.all()
    data = {
        'info': info
    }
    return render(request, 'main/about.html', {'data': data})
def musix(request):
    song = Song.objects.all()
    song_data = {
        'song': song
    }
    return render(request, 'main/musix.html', {'song_data': song_data})
def test(request):
    return render(request, 'main/test.html')