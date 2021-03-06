"""atestado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from atestado import settings
from app.views import entrar, sair, submit, home, pesquisa, searchall, form, create, view, edit, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entrar', entrar, name='entrar'),
    path('sair', sair, name='sair'),
    path('entrar/submit/', submit, name='submit'),
    path('', home, name='home'),
    path('pesquisa/', pesquisa, name='pesquisa'),
    path('pesquisa/searchall/', searchall, name='searchall'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('pesquisa/view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
