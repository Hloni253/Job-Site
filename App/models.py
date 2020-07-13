from django.db import models
from django.urls import reverse


class JobCategory(models.Model):
    title = models.CharField(max_length=100)
    job_url = models.CharField(max_length=100)
    number_of_jobs = models.IntegerField()
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
        
    @property
    def jobs(self):
        return self.job_set.all()
    
    def my_url(self):
        return reverse('App:jobs', kwargs={'slug':self.slug})
        
class Job(models.Model):
    title = models.CharField(max_length=100)
    job_url = models.CharField(max_length=100)
    job_category = models.ForeignKey(JobCategory, models.CASCADE)
    region = models.CharField(max_length=100)
    days_left = models.IntegerField()
    
    def __str__(self):
        return self.title