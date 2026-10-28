from django.db import models
class Department(models.Model):
    name=models.CharField(max_length=100, unique=True)
    description=models.TextField(blank=True)
    class Meta: ordering=["name"]
    def __str__(self): return self.name

class Employee(models.Model):
    GENDER_CHOICES=[("Male","Male"),("Female","Female"),("Other","Other")]
    HOBBY_CHOICES=[("Reading","Reading"),("Music","Music"),("Sports","Sports"),("Traveling","Traveling"),("Gaming","Gaming")]
    name=models.CharField(max_length=120)
    age=models.PositiveSmallIntegerField()
    department=models.ForeignKey(Department,on_delete=models.PROTECT,related_name="employees")
    profile_photo=models.ImageField(upload_to="employee_photos/",blank=True,null=True)
    hobbies=models.JSONField(default=list,blank=True)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    email=models.EmailField()
    class Meta: ordering=["name"]
    def __str__(self): return self.name
