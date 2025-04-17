from django.contrib import admin
from django.urls import path,include
from . import views 
# app_name = "accounts" 
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("register",views.register, name="register"),
#     path("login_view",views.login_view, name="login_view"),
#     path("logout",views.logout, name="logout"),

    
# ]


from django.urls import path
from .views import RegisterView, LoginView, LogoutView

app_name = "accounts"

urlpatterns = [
    

    path("register/", RegisterView.as_view(), name="register"),
    # path("login/", LoginView.as_view(), name="login_view"),
    path("login/", LoginView.as_view(), name="login_view"),
#     path("logout/", LogoutView.as_view(), name="logout_view"),
    path("logout/", LogoutView.as_view(), name="logout_view")
]
