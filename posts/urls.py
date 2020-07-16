from django.urls import path
from .views import *

app_name="posts"
urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('', main, name="main"),
    path('<int:post_id>/', show, name="show"),
    path('<int:post_id>/edit/', update, name="update"),
    path('<int:post_id>/delete/', delete, name="delete"),
]