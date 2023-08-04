# shortener/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_url_obj, created = ShortURL.objects.get_or_create(long_url=long_url)
        short_url = request.build_absolute_uri('/') + short_url_obj.short_code
        return render(request, 'result.html', {'short_url': short_url})
    return render(request, 'index.html')

def redirect_to_long_url(request, short_code):
    short_url_obj = get_object_or_404(ShortURL, short_code=short_code)
    short_url_obj.clicks += 1
    short_url_obj.save()
    return redirect(short_url_obj.long_url)

def not_found(request, exception):
    return render(request, '404.html', status=404)
