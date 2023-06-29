from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.Search, name="search"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("newproduct", views.NewProduct, name="NewProduct"),
    path("product/<int:product_id>", views.product_view, name="product"),
    path("neworder", views.NewOrder, name="NewOrder"),
    path("orders", views.Orders_views, name="orders"),
    path("profile", views.profile_views, name="profile"),
    path("profilesave", views.profile_save, name="profilesave"),
    path("about", views.About, name="about")
    
]