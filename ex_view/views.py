from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render # 템플릿 선택해서 응답줄떄

from django.utils import timezone
from django.urls import reverse

# Create your views here.

def index(request):
    now = timezone.now()
    print('현재시간:' , now)
    print(reverse('exview:index')) # 경로를 만들 때 파라미터가 없었음
    print(reverse('exview:get1')) # 얘도 파라미터 없었음
    print(reverse('exview:get2', args=(11,22,'hello'))) # 하지만 get2는 get2/?/?/?/ 이 경로를 만들기 위해서 거기에 들어갈 값이 필요한데 그걸 args을 이용할 수 있음
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

# 클래스형 뷰
from django.views.generic import View # 클래스 형 뷰는 제네릭 뷰 라고해서 일반적인 웹서비스에 필요한 동작들에 대해서 장고에서 미리 만들어논 뷰
# 사용자한테 폼을 보여주는 기능
# 사용자한테 데이터베이스 내용을 목록으로 보여주는 일반적인 기능들을 가지고 있다

class ExamGet3(View): # View를 상속 View로 사용 할 클래스는 View를 상속받게 되어있다
    
    def get(self, request):
        print('get3/ 요청이 들어옴')
        print(request.GET)
        print(request.GET['n1'] + request.GET['n2']) # 문자열
        print(int(request.GET['n1']) + int(request.GET['n2'])) # 형변환
        return HttpResponse('get3')
    
class ExamGet4(View): # View를 상속
    def get(self, request, n1, n2, n3): # get 요청을 처리할 때는 get 메소드를 이용한다
        print('n1:', n1)
        print('n2:', n2)
        print('n3:', n3)
        print(n1 + n2) # 이미 urls 경로상에서 int라고 지정했기에 정수형으로 들어옴
        return HttpResponse('get4')
    
class ExamPost3(View):
    def post(self, request):
        print('post3/ 요청이 들어옴')
        keys = request.POST.keys()
        print(request.POST['n1'] + request.POST['n2']) 
        for key in keys:
            value = request.POST[key]
            print(f'{key} : {value}')
        return HttpResponse('post3')
    
class ExamPost4(View):
    def post(self, request, msg, n):
        print('post4/ 요청이 들어옴')
        print('msg:', msg)
        print('n:', n)
        keys = request.POST.keys()
        print(request.POST['n1'] + request.POST['n2']) 
        for key in keys:
            value = request.POST[key]
            print(f'{key} : {value}')
        return HttpResponse('post4')
    
class ExamGetPost(View):
    def get(self, request):
        print('GET요청 동작')
        return HttpResponse('getpost2/(GET)')
    
    def post(self, request):
        print('POST요청 동작')
        user = request.POST['user']
        pwd = request.POST['pwd']
        if user == pwd:
            print('로그인 성공')
            return HttpResponse('getpost2/(POST)')
        else:
            print('로그인 실패(다시 폼 전송)')
            return HttpResponseRedirect(reverse('exview:index')) # 로그인 실패하였습니다 팝업창 뜨게하고 로그인 페이지 보이게 하면 될듯