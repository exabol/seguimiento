from django.urls import URLPattern, path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('ilcs', views.ilcs, name='ilcs'),
    path('ilcs/crear', views.crear, name='crear'),
    path('ilcs/editar', views.crear, name='editar'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)