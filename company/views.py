from django.views.generic.base import TemplateView

from common.views import CommonContextMixin


class AboutView(CommonContextMixin, TemplateView):
    template_name = 'company/about.html'
    title = 'About 🌼 Fun Flowers'


class ContactView(CommonContextMixin, TemplateView):
    template_name = 'company/contact.html'
    title = 'Contact 🌼 Fun Flowers'


class GalleryView(CommonContextMixin, TemplateView):
    template_name = 'company/gallery.html'
    title = 'Gallery 🌼 Fun Flowers'
