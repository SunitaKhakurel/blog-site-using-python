from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author =models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title =models.CharField(max_length=200)
    text =models.TextField()
    created_date = models.DateField(auto_now_add=True)
    published_date =models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def approve_comments(self):
        return self.comments.filter(approced_comment=True)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title


class Comment(models.Model):
    post =models.ForeignKey('blog.Post', related_name='comments',on_delete=models.DO_NOTHING)
    author =models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    approved_comment =models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment =True
        self.save()
    
    def get_absolute_url(self):
        return reverse("post_list")
    

    def __str__(self):
        return self.text

