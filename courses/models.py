from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.loader import render_to_string
from .fields import OrderField

class Subject(models.Model):
    title   = models.CharField(max_length=200)
    slug    = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
# c = Course.objects.get(id=3)
# c.students.all()
# c.subject
# c.owner
# c.modules.get(id=9)
# obj = c.modules.get(id=9)
# obj.contents.all()
# new_obj = Course.objects.filter(modules__id='9')
# new_obj = Course.objects.filter(modules__title__contains='health')
# new_obj = Course.objects.filter(modules__contents__content_type='1')
# <QuerySet []>
# from django.contrib.auth.models import User
# u = User.objects.get(id=1)
# u.courses_joined.all()
# u.courses_created.all()
class Course(models.Model):
    owner       = models.ForeignKey(User,related_name='courses_created',on_delete=models.CASCADE)
    subject     = models.ForeignKey(Subject,related_name='courses',on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    picture     = models.ImageField(upload_to='img/', blank=True, null=True)
    slug        = models.SlugField(max_length=200, unique=True)
    overview    = models.TextField()
    created     = models.DateTimeField(auto_now_add=True)
    students    = models.ManyToManyField(User, related_name='courses_joined', blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('student_course_detail', kwargs={'slug':self.slug})

class Module(models.Model):
    course      = models.ForeignKey(Course,related_name='modules',on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order       = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.id}'
    
    # def get_absolute_url(self):
    #     return reverse('student_course_detail_module', kwargs={'id':self.id})

class Content(models.Model):
    module          = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model_in':(
        'text', 'video', 'image', 'file')})
    object_id       = models.PositiveIntegerField()
    item            = GenericForeignKey('content_type', 'object_id')
    order           = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']

class ItemBase(models.Model):
    owner   = models.ForeignKey(User,related_name='%(class)s_related',on_delete=models.CASCADE)
    title   = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string(f"courses/content/{self._meta.model_name}.html", {'item':self})

class Text(ItemBase):
    content = models.TextField()
class File(ItemBase):
    file = models.FileField(upload_to='files')
class Image(ItemBase):
    file = models.FileField(upload_to='images')
class Video(ItemBase):
    url = models.URLField()