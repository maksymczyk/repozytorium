from django.views.generic import TemplateView


class AboutPageView(TemplateView):
    template_name = 'about.html'

class GalleryPageView(TemplateView):
    template_name = 'gallery.html'

class BasePageView(TemplateView):
    template_name = 'base.html'

class HomePageView(TemplateView):
    template_name = 'home.html'
