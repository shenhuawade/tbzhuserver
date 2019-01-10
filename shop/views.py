import json
from django.shortcuts import render
from django.http import HttpResponse
from shop import models
from django.http import JsonResponse
# Create your views here.
import top.api
import http.client
# 这里填写你申请到的APPkey

# 配置阿里SDK
appkey = '25541421'
secret = '04ede9704b4da9fd2d13eecd3b37e60d'
url = 'gw.api.taobao.com'
port = 80
# 好券清单API（导购）只能搜索有券,搜索类目商品，自动高佣金
def getHaoQuan_list_items(request):
    req = top.api.TbkDgItemCouponGetRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    print(appkey)
    req.adzone_id = 80892900374
    req.platform =2
    req.cat = "16,18"
    req.page_size = 20
    req.q = "女装"
    req.page_no = 1
    try:
        resp = req.getResponse()
        # print(type(resp))
        # print(resp)
        print(type(JsonResponse(resp)))
        return JsonResponse(resp)
    except Exception as e:
        print(e)
        return JsonResponse({"msg": "service error!!"})





def index(request):
    return HttpResponse('你好，这是我第一个程序')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def home(request):
    return render(request,'home.html')

def add2(request,a,b):
    models.addPserson()
    c = int(a) + int(b)
    return HttpResponse(str(c))

