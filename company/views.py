from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    template_name = 'company/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data()
        context['title'] = 'About 🌼 Fun Flowers'
        return context


class ContactView(TemplateView):
    template_name = 'company/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data()
        context['title'] = 'Contact 🌼 Fun Flowers'
        return context


class GalleryView(TemplateView):
    template_name = 'company/gallery.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data()
        context['title'] = 'Gallery 🌼 Fun Flowers'
        return context
