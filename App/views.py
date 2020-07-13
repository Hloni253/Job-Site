from django.shortcuts import render, redirect
from .models import JobCategory, Job
from .forms import JobCategoryForm, JobForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import JobSerializers, JobCategorySerializers

def home(request):
    categories = JobCategory.objects.all()
    
    objs = {
        'categories':categories
    }
    
    return render(request, 'App/home.html', objs)
    
def create_category(request):
    form = JobCategoryForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('App:home')
        
    objs = {
        'form':form
    }
    
    return render(request, 'App/create_category.html', objs)
    
def create_job(request):
    form = JobForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('App:home')
        
    objs = {
        'form':form
    }
    
    return render(request, 'App/create_job.html', objs)
    
def jobs(request, slug):
    category_q = JobCategory.objects.filter(slug=slug)
    
    if category_q.exists():
        category = category_q.first()
        
    objs = {
        'category':category
    }
    
    return render(request, 'App/jobs.html', objs)


@api_view(['GET', 'POST'])
def job_list(request):
    if request.method == 'GET':
        data = Job.objects.all()
        
        serializer = JobSerializers(data, context={'request':request}, many=True)
        
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = JobSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def job_category_list(request):
    if request.method == 'GET':
        data = JobCategory.objects.all()

        serializer = JobCategorySerializers(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = JobCategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT','DELETE'])
def jobs_detail(request,id):
    try:
        jobs = JobCategory.get(id=id)
    except JobCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = JobCategorySerializers(jobs, data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












