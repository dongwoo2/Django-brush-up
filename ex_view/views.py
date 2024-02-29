from django.http import HttpResponse
from django.shortcuts import render # 템플릿 선택해서 응답줄떄

from django.utils import timezone

# Create your views here.

def index(request):
    now = timezone.now()
    print('현재시간:' , now)
    return render(request, "ex_view/index.html", {'now' :now}) # 'now' now는 템플릿에서 사용할 이름 다른 이름을 이용해도 됨 딕셔너리 형태
