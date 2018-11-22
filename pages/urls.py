from django.urls import path

from .views import AboutPageView, HomePageView, GalleryPageView, BasePageView

urlpatterns = [
    path('home/', HomePageView.as_view(), name= 'home'),
    path('', BasePageView.as_view(), name='base'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
]
