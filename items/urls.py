from django.urls import path
from .views import all_items_view, item_detail_view, delete_item_view

app_name = 'items'


urlpatterns = [
    # path('', index_view, name='home'),
    # path('items/', ItemsListView.as_view(), name='list'),
    path('', all_items_view, name='list'),
    # path('items/<pk>', ItemDetailView.as_view(), name='details'),
    path('items/<int:pk>', item_detail_view, name='details'),
    path('<int:pk>/delete', delete_item_view, name='delete'),
]
