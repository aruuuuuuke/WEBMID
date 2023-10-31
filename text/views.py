from django.shortcuts import render
from text.models import Text

def all_news(request):
    if request.method =='GET':
        news=Text.objects.all()
        context={
            'news': news
        }
        return render(request, template_name='news.html', context=context)

def empty(request):
    if request.method == 'GET':
        return render(request, 'site.html')
    
def detail(request,id):
    if request.method=='GET':
        text=Text.objects.get(id=id)
        context = {
            'text' :text
        }
        return render(request, template_name='detail.html', context=context)