from django.urls import path
import views as menu

urlpatterns = [
    path(r'^', menu.index, name='index'),
    path(r'^(\d+)', menu.index, name='index')
]
