from django.conf.urls.static import static
from django.contrib import admin
from jahongir import settings
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/languages/', language_list, name='language_list'),
    path('api/navbars/', navbar_list, name='navbar_list'),
    path('api/categories/', category_list, name='category_list'),
    path('api/informations/', information_list, name='information_list'),
    path('api/contacts/', contact_list, name='contact_list'),
    path('api/news/', news_list, name='news_list'),
    path('api/donates/', donate, name='donate'),
    path('api/jointogroups/',jointogroup, name='jointogroup'),
    path('api/regions/', region_list, name='region_list'),
    path('api/famous/', famous_personalities_list, name='famous_personalities_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)