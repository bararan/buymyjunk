from django.urls import path
from .views import messagebox_view#MsgBoxView

app_name = 'messaging'

urlpatterns = [
    # path('', MsgBoxView.as_view(), name='messagebox')
    path('', messagebox_view, name='messagebox')
]
