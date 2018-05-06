from django.db import models


# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=120)
    project_owner = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
