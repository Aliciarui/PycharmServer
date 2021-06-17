from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_view),
    path('index/',views.loginsuc),
    path('trial/',views.trial)
]