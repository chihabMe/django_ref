from multiprocessing import context
from django.shortcuts import redirect, render,reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def login_view(request):
    context={}
    if not request.user.is_authenticated:
        if request.method=="POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            if username and password:
                user = authenticate(username=username,password=password)
                if user :
                    login(request,user)
                    return redirect(reverse("articles:home"))
                context["error"]="the password or the username is uncorect"
        return render(request,'accounts/login.html',context)
    return redirect(reverse("articles:home"))
def logout_view(request):
    logout(request)
    return redirect(reverse("accounts:login"))
