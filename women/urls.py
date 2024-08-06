from .views import *
from django.urls import path, re_path

urlpatterns = [

    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name = 'category'),
    #path('cats/', categories),
    path('cats/<int:catid>', categories),
    re_path(r'archive/(?P<year>[0-9]{4})', archive),
]

