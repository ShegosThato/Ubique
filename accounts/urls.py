from django.urls import path
from . import views

app_name = 'ubi'

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/<int:person_id>', views.accounts, name='accounts'),
    path('search/<int: person_id>', views.search_by_id, name='search'),
    path('accounts/<int:person_id>/delete', views.delete_acc, name='delete_acc'),
    path('accounts/add', views.add, name='add'),
]