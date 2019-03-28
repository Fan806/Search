from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from . import models


# Create your views here.
def index(request):
    # return HttpResponse("hello world!")
    return render(request, "index.html",)

@login_required
def form(request):
    if request.method=="POST":
        username = request.user.username
        user = models.User.objects.get(name=username)
        name = request.POST.get("name", None)
        bachelor = request.POST.get("bachelor", None)
        master = request.POST.get("master", None)
        phd = request.POST.get("phd", None)
        print(name,bachelor,master,phd)

    return render(request, "form.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get('Name',None)
        password = request.POST.get('password',None)
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
    return render(request, "register.html")