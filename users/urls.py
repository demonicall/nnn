from django.urls import path
from .views import register_view, CookieLoginView, logout_view, UserDetailView

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", CookieLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]
