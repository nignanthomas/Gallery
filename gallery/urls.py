from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$',views.landing,name='landing'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^category/(\w+)', views.page_category,name='page_category'),
    url(r'^location/(\w+)', views.page_location,name='page_location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
