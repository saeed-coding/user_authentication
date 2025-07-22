"""
URL configuration for mysite1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import *
from vege.views import *
from api.views import *
from products_api.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # API Views
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('recipes/', RecipeListCreate.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),

    # Product Views
    path('products/', get_products, name='get_products'),
    path('create_product/', create_product, name='create_product'),
    path('update_product/', update_product, name='update_product'),
    path('delete_product/', delete_product, name='delete_product'),

    # Vege Views
    path('recipe/', recipes, name='recipes'),
    path('delete_recipe/<id>/', delete_recipe, name='delete_recipe'),
    path('update_recipe/<id>/', update_recipe, name='update_recipe'),
    path("register_recipe/", register_recipe, name="register_recipe"),
    path("login_recipe/", login_recipe, name="login_recipe"),
    path("logout_recipe/", logout_recipe, name="logout_recipe"),

    # Blog Views
    path('', home, name="home"),
    path("contact/", contact_page, name="contact"),
    path("success_page/", success_page, name="success"),
    path("about/", about_page, name="about"),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
