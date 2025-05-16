from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ShortenedURL
from django.utils.crypto import get_random_string
from django.urls import reverse


def home(request):
    message = ''
    short_url = None
    original_url = None
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        custom_code = request.POST.get('custom_code')
        if custom_code:
            if ShortenedURL.objects.filter(short_code=custom_code).exists():
                message = 'Custom short code is already taken.'
            else:
                short_code = custom_code
        else:
            # Generate a random short code
            short_code = get_random_string(6)
            while ShortenedURL.objects.filter(short_code=short_code).exists():
                short_code = get_random_string(6)
        if not message:
            shortened = ShortenedURL.objects.create(
                original_url=original_url,
                short_code=short_code
            )
            short_url = request.build_absolute_uri(reverse('shortener:redirect', args=[short_code]))
    return render(request, 'shortener/home.html', {'message': message, 'short_url': short_url, 'original_url': original_url})

def redirect_short_url(request, short_code):
    url_obj = get_object_or_404(ShortenedURL, short_code=short_code)
    url_obj.click_count += 1
    url_obj.save()
    return redirect(url_obj.original_url)

def stats(request):
    urls = ShortenedURL.objects.all().order_by('-created_at')
    return render(request, 'shortener/stats.html', {'urls': urls})
