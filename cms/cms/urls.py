"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from api.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<str:username>/<str:password>/<str:api_key>', data_view),
    path('', home),
    path('view/<int:post_id>', view_blog),
    path('update/<int:post_id>', modify_blog),
    path('create_blog', create_blog),
    path('create_user', create_user),
    path('save/<path:img_link>',show_images),
    path('delete/<int:post_id>/',delete_post),
    path('delete/<int:post_id>/<int:confirmation>',delete_post),

]
