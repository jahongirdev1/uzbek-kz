from django.conf.urls.static import static
from django.contrib import admin
from jahongir import settings
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('languages/', language_list, name='language_list'),
    path('navbars/', navbar_list, name='navbar_list'),
    path('categories/', category_list, name='category_list'),
    path('informations/', information_list, name='information_list'),
    path('contacts/', contact_list, name='contact_list'),
    path('news/', news_list, name='news_list'),
    path('donates/', donate, name='donate'),
    path('jointogroups/',jointogroup, name='jointogroup'),
    path('regions/', region_list, name='region_list'),
    path('famous/', famous_personalities_list, name='famous_personalities_list'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)