from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import os
from questions.models import Question


class Objective(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    questions = models.ManyToManyField(Question)
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    public = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Chapter(models.Model):
    book = models.ForeignKey(Book)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    order = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['order']


class Section(models.Model):
    name = models.CharField(max_length=120)
    chapter = models.ForeignKey(Chapter)
    description = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    objectives = models.ManyToManyField(Objective)
    order = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['order']


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Textbook(models.Model):
    title = models.CharField(max_length=200)
    edition = models.CharField(max_length=10)
    authors = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True, upload_to=get_image_path)
    def __str__(self):
        return "{title}, {edition} ed.".format(
                title=self.title, edition=self.edition)


class CourseType(models.Model):
    name = models.CharField(max_length=200)
    book = models.ForeignKey(Book)
    textbook = models.ForeignKey(Textbook, blank=True, null=True)
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    instructor = models.ForeignKey(User)
    start_date = models.DateField()
    end_date = models.DateField()
    semester = models.CharField(max_length=50)
    assistants = models.ManyToManyField(
        User, related_name='assisting_courses', blank=True
    )
    course_type = models.ForeignKey(CourseType)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return "{0} ({1})".format(self.name, self.instructor)
    def display(self):
        if self.semester:
            return '{0} ({1})'.format(self.name, self.semester)
        return self.name
    def get_absolute_url(self):
        return reverse('CourseDetails', args=(str(self.id),))
    



