from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.ContactUsCreatView.as_view(), name='contact_us'),
]
