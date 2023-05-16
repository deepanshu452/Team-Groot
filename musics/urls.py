from musics.views import addMusic, homePage
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
app_name='musics'

urlpatterns = [
    path('',homePage,name='home_page'), 
    path('add/',addMusic,name='add_music'), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
