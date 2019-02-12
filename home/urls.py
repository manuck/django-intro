from django.urls import path
# home 폴더 내에 있는 views.py를 불러온다.
from . import views

urlpatterns = [
    # 요청이 으로 오면, views의 index 함수를 실행시킨다.
    path('', views.index),
    path('dinner/', views.dinner),
    path('you/<name>/', views.you),
    path('cube/<int:num>/', views.cube),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('user_new/', views.user_new),
    path('user_read/', views.user_read),
    path('template_example/', views.template_example),
    path('static_example/', views.static_example),
]
