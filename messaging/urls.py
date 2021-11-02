from django.urls import path
from .views import messagebox_view

app_name = 'messaging'

urlpatterns = [
    path('', messagebox_view, name='messagebox')
]
