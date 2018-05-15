# django-rest-sandbox

C:\Users\User\.virtualenvs\django-rest-sandbox\Scripts>activate

pip freeze > requirements.txt

python manage.py migrate
python manage.py makemigrations

python manage.py createsuperuser
python manage.py runserver
pip install -Ur requirements.txt # Install Django via pip installing all dependencies in requirements.txt

flo
12qw12qw

## Tutorials
LINKS
######
https://medium.com/@djstein/modern-django-part-1-project-refactor-and-meeting-the-django-settings-api-d2784efb606f
######
http://www.django-rest-framework.org/#installation
https://medium.com/netscape/full-stack-django-quick-start-with-jwt-auth-and-react-redux-part-i-37853685ab57
https://pythonprogramming.net/first-site-django-python-tutorial/?completed=/django-web-development-with-python-intro/
https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1
https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
https://medium.com/@djstein/modern-django-part-0-introduction-and-initial-setup-657df48f08f8

# New Model
1. Neues Model unter api/models | class Project(models.Model)
2. Serializer api/serializers | class ProjectSerializer(serializers.HyperlinkedModelSerializer)
3. url api/urls | router.register(r'projects', views.ProjectViewSet)
4. view api/views | class ProjectViewSet(viewsets.ModelViewSet):
! Migrate nicht vergessen
