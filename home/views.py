from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def dinner(request):
    box = ['치킨', '서브웨이', '맥날', '롯데리아']
    dinner = random.choice(box)
    # render 필수인자
    # 1) request, 2) template 파일(html)
    # render 선택인자
    # 3) dictionary : 템플릿에서 쓸 변수 값을 정의
    return render(request, 'dinner.html', {'dinner' : dinner, 'box' : box})
    # template은 기본적으로 문법이 jinja2랑 비슷한데, 장고에서는 DTL을 쓴다.
    # Django Template Language
    
def you(request, name):
    return render(request, 'you.html', {'name': name})

def cube(request, num):
    result = num**3
    return render(request, 'cube.html', {'num' : num, 'result':result})