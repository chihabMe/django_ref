from multiprocessing import context
from re import T
from wsgiref.util import request_uri
from django.shortcuts import redirect, render,reverse
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleCreatForm
# Create your views here.
@login_required
def home(request):
    articles = Article.objects.all()

    context = {
        "articles":articles
    }
    return render(request,"articles/home.html",context)
@login_required
def article_create(request):
    form = ArticleCreatForm()
    if request.method=="POST":
        form = ArticleCreatForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data.get("title")
            # body = form.cleaned_data.get("body")
            # Article.objects.create(title=title,body=body)
            form.save()
            return redirect(reverse("articles:home"))

    context = {
        'form':form
    }
    return render(request,'articles/create.html',context)
def article(request,id):

    obj = Article.objects.get(id=id)
    context = {
        "article":obj
    }
    return render(request,"articles/detail.html",context)
@login_required
def search(request):
    q = request.GET.get("q")
    if q is not None:
        articles = Article.objects.filter(title__icontains=q)
        if articles.count()==0:
            articles=None
    context = {
        "articles":articles
    }
    return render(request,'articles/search.html',context)