from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls',namespace='App')),
    re_path(r'^api/jobs', views.job_list),
    re_path(r'^api/categories', views.job_category_list),
    re_path(r'^api/categories/[0-9]', views.jobs_detail),
]
