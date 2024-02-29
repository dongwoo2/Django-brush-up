from django.urls import path

from .import views # 현재 패키지에서 views를 임포트한다.

urlpatterns = [
    path('', views.index)
]