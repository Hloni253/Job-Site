from django import forms
from .models import JobCategory, Job

class JobCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = ['title','job_url','number_of_jobs','slug']
        
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','job_url','job_category','region','days_left']