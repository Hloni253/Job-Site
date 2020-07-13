from django.urls import path
from .views import home, create_category, create_job, jobs

app_name='App'
urlpatterns = [
    path('', home, name='home'),
    path('create/category', create_category, name='create category'),
    path('create/job', create_job, name='create job'),
    path('<slug>/', jobs, name='jobs'),
]