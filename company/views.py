from django.shortcuts import render

# Create your views here.


def about(request):
    context = {
        'title': 'About 🌼 Fun Flowers'
    }
    return render(request, 'company/about.html', context)


def contact(request):
    context = {
        'title': 'Contact 🌼 Fun Flowers',
    }
    return render(request, 'company/contact.html', context)


def gallery(request):
    context = {
        'title': 'Gallery 🌼 Fun Flowers',
    }
    return render(request, 'company/gallery.html', context)
