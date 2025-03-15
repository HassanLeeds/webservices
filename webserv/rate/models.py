from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professor (models.Model):
    id = models.CharField(unique=True, max_length = 8, primary_key=True)
    name = models.CharField(max_length = 40)
    
    def __str__ (self):
        return self.name

class Module (models.Model):
    code = models.CharField(unique=True, max_length = 10, primary_key=True)
    desc = models.CharField(max_length = 100)

    def __str__ (self):
        return self.desc

class ModuleInstance (models.Model):
    professor = models.ManyToManyField(Professor)
    year = models.IntegerField()
    sem = models.IntegerField(choices=[(1, "1"), (2, "2")], null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    
    def __str__ (self):
        return f"{self.module.code} {self.year} {self.sem}"


class Rating (models.Model):
    stars = models.IntegerField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")])
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    module_instance = models.ForeignKey(ModuleInstance, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    class Meta:
        unique_together = ('user', 'professor', 'module_instance')

    def __str__ (self):
        return f"{self.module_instance.module.code} {self.professor.id} {self.stars}"


