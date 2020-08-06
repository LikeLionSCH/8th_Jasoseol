from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
        # on_delete=models.CASCADE
        # foreignkey로 연결된 object가 지워질때, 연결된 자소설 object도 지워짐
        # 작성자 회원 탈퇴 시 자소서들도 삭제됨을 의미
        
        # null=True
        # 빈 값도 허용

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    jasoseol = models.ForeignKey(Jasoseol, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    