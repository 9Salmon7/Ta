from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = "base.html"

class P1View(TemplateView):
	template_name = "P1.html"


def index(request):
    # コンテキストデータを定義する
    context = {
        'username': 'John',
        'email': 'john@example.com'
    }
    # テンプレートをレンダリングしてレスポンスとして返す
    return render(request, 'base.html', context)