from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.views.generic import View
from ..forms import UserForm

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as logout_user
from django.shortcuts import redirect


def logout(request):
    logout_user(request)
    return redirect("index")


@csrf_protect
def login(request, *args, **kwargs):
    template_name = "login.html"
    context = {}

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect("index")
    elif request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        context["success"] = False
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect("index")

    return render(request, template_name, context)


class register(View):
    template_name = "register.html"
    form = UserForm

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

    method_decorator(csrf_protect)
    def post(self, request,*args,**kwargs):
        data = request.POST.copy()

        form = self.form(data=data)
        context = {"success": False}

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()

            user1 = authenticate(username=username, password=password)

            context["success"] = True
            redirectTo ='index'

            if user1 is not None:
                if user.is_active:
                    login(request, user1)
                    redirectTo = 'index'

            return redirect(redirectTo)

        return render(request, self.template_name, context)
