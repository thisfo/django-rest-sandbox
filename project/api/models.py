from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=120)
    owner = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title
