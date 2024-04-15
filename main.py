# Cell 1: Create Your First Django Project
django-admin startproject mysite .

# Cell 2: Define Django Models and Apply Migrations
# Assuming your app is named 'myapp', add this model to myapp/models.py
from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

# Make migrations for the new model
python manage.py makemigrations

# Apply migrations to the database
python manage.py migrate

# Cell 3: Set Up the Django Admin Interface
# Register the model in myapp/admin.py
from django.contrib import admin
from .models import Post
admin.site.register(Post)

# Create a superuser
python manage.py createsuperuser

# Cell 4: Create a GitHub Repository for Your Django Project
# Initialize Git and commit the project
git init
git add .
git commit -m 'Initial commit of Django project'
git remote add origin https://github.com/yourusername/yourrepositoryname.git
git push -u origin main
"""
with open('django_project_setup_instructions.txt', 'w') as file:
    file.write(instructions)
print('Instructions saved to django_project_setup_instructions.txt')