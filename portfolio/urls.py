from django.urls import path
from .templates.portfolio import views

urlpatterns = [
    # path(URL extension, Python function, internal name)
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]