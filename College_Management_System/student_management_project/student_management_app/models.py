from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class SessionYearModel(models.Model):
    id=models.AutoField(primary_key=True)
    session_year_start=models.DateField()
    session_year_end=models.DateField()
    objects=models.Manager()

class CustomUser(AbstractUser):
    HOD='1'
    STAFF='2'
    STUDENT='3'

    EMAIL_TO_USER_TYPE_MAP={
        'hod':HOD,
        'staff':STAFF,
        'student':STUDENT
    }
    
    user_type_data=((HOD,'HOD'),(STAFF,'Staff'),(STUDENT,'Student'))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    created_by=models.DateTimeField(auto_now_add=True)
    updated_by=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE,default=1)
    staff_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender=models.CharField(max_length=50)
    profile_pic=models.FileField()
    address=models.TextField()
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING,default=1)
    session_year_id=models.ForeignKey(SessionYearModel,null=True,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()


