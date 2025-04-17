# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.contrib.auth import logout,authenticate, login


# from django.contrib.auth import logout as django_logout



# def register(request):
#     if request.method == "POST":
#         firstname = request.POST.get("firstname")
#         lastname = request.POST.get("lastname")
#         username = request.POST.get("username")  # Ensure username is retrieved
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")

#         if not username:  # Ensure username is not empty
#             messages.error(request, "Username is required.")
#             return redirect("accounts:register")  

#         if password != confirm_password:
#             messages.error(request, "Passwords do not match.")
#             return redirect("accounts:register")  

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists.")
#             return redirect("accounts:register")

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already registered.")
#             return redirect("accounts:register")

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password,
#             first_name=firstname,
#             last_name=lastname,
#         )
#         user.save()
#         print("Account created successfully!")
#         messages.success(request, "Account created successfully!")
#         return redirect("accounts:login_view")  

#         # return redirect("home")
#     else:
#         return render(request, "account/register.html")



# def login_view(request):  
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(request, username=username, password=password)  

#         if user is not None:
#             login(request, user)  
#             messages.success(request, "Login successful!")
#             return redirect("quizengine:home") 
#         else:
#             messages.error(request, "Invalid username or password.")
#             return redirect("account:login_view")
#         # return render(request, "account/login.html") 
#     else:
#         return render(request, "account/login.html")


# def logout(request):
#     django_logout(request)  
#     return redirect("quizengine:home")


from django.views.generic import FormView, View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserLoginForm
from django.shortcuts import render


class RegisterView(FormView):
    template_name = "account/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("accounts:login_view")

    def form_valid(self, form):
        try:
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            messages.success(self.request, "Account created successfully!")
        except Exception as e:
            messages.error(self.request, f"Something went wrong: {str(e)}")
            return self.form_invalid(form)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "account/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("quizengine:home")

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            login(self.request, user)
            messages.success(self.request, "Login successful!")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid username or password.")
            return redirect("accounts:login_view")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("quizengine:home")
