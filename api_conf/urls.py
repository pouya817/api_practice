from django.urls import path
from . import views
urlpatterns=[
    path('call_api/', views.helloapi.as_view() )
]