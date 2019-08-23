from django.shortcuts import render, render_to_response, redirect  # 导入render和render_to_reponse模块

# 先定义一个数据列表，当然后面熟了可以从数据库里取出来
list = [{"name": 'good', 'password': 'python'}, {'name': 'learning', 'password': 'django'}]


def index(request):
    return render_to_response('index.html')


def edu(request):
  return render_to_response('Education.html')

def info(request):
    return render_to_response('Information.html')


def trans(request):
    return render_to_response('Transformation.html')

def cla(request):
    return render_to_response('Classification.html')

def calcu(request):
    return render_to_response('Calculator.html')
