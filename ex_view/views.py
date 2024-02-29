from django.http import HttpResponse
from django.shortcuts import render # 템플릿 선택해서 응답줄떄

from django.utils import timezone

# Create your views here.

def index(request):
    now = timezone.now()
    print('현재시간:' , now)
    return render(request, "ex_view/index.html", {'now' :now}) # 'now' now는 템플릿에서 사용할 이름 다른 이름을 이용해도 됨 딕셔너리 형태


def get1(request): # 요청응답에 사용되는 모든데이터는 전부 다 문자열
    print('get1/ 요청이 들어옴')
    print(request.GET)
    print(request.GET['n1'] + request.GET['n2']) # 문자열
    print(int(request.GET['n1']) + int(request.GET['n2'])) # 형변환
    return HttpResponse('get1')

def get2(request, n1, n2, n3):
    print('n1:', n1)
    print('n2:', n2)
    print('n3:', n3)
    print(n1 + n2) # 이미 urls 경로상에서 int라고 지정했기에 정수형으로 들어옴
    return HttpResponse('get2')

def post1(request): 
    print('post1/ 요청이 들어옴')
    print(request.POST)
    print(int(request.POST['n1']) + int(request.POST['n2'])) 
    return HttpResponse('post1')

def post2(request, msg, n): #msg 파라미터는 post2/hello/123/ form에서 hello받아주는 파마리터는 , n은 123
    print('post2/ 요청이 들어옴')
    print('msg:', msg)
    print('n:', n)
    print(request.POST)
    print(int(request.POST['n1']) + int(request.POST['n2'])) 
    return HttpResponse('post2')

def getpost1(request):
    print(request.method)
    if request.method == 'GET':
        print('GET 요청에 대한 처리') # 사용자 입력 폼(login)
    elif request.method == 'POST':
        print('POST 요청에 대한 처리') # 입력 값 처리(login process)
    return HttpResponse('getpost1')