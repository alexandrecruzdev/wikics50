from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage/", views.newpage, name="newpage"),
    path("randompage/", views.randompage, name="randompage"),
    path("similarpages/<str:title>", views.similarpages, name="similarpages"),
    path("editpage/<str:title>", views.editpage, name="editpage"),
    path("wiki/<str:title>", views.get_encyclopedia, name="get_encyclopedia")
]
