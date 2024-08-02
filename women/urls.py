from .views import *
from django.urls import path, re_path

urlpatterns = [

    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name = 'category'),
    #path('cats/', categories),
    path('cats/<int:catid>', categories),
    re_path(r'archive/(?P<year>[0-9]{4})', archive),
]

