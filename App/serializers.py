from rest_framework import serializers
from .models import Job, JobCategory

class JobCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ('slug','title','job_url','number_of_jobs')

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id','title','job_url','job_category','region','days_left')