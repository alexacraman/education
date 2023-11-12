import code
from rest_framework import serializers
from ..models import Subject, Course, Module, Content


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']



class ModuleSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerialzer(many=True, read_only=True)
    class Meta:
        model = Course 
        fields = ['id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules']


class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()

class ContentSerializer(serializers.ModelSerializer):
    item = ItemRelatedField(read_only=True)

    class Meta:
        model = Content 
        fields = ['order', 'item']

class ModuleWithContentsSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)

    
    class Meta:
        model = Module
        fields = ['order', 'title', 'description', 'contents']


class CourseWithContentsSerializer(serializers.ModelSerializer):
    modules =  ModuleWithContentsSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules']
    
# driver code
# >>> from courses.models import Subject
# >>> from courses.api.serializers import SubjectSerializer
# >>> subject = Subject.objects.latest('id')
# >>> subject
# <Subject: Fire Safety>
# >>> serializer = SubjectSerializer(subject)
# >>> serializer.data
# {'id': 5, 'title': 'Fire Safety', 'slug': 'fire-safety'}
# >>> from io import BytesIO
# >>> from rest_framework.parsers import JSONParser
# >>> data = b'{"id":4, "title":"Programmer", "slug":"programming"}'
# >>> JSONParser().parse(BytesIO(data))
# {'id': 4, 'title': 'Programmer', 'slug': 'programming'}
# >>> from rest_framework.renderers import JSONRenderer
# >>> JSONRenderer().render(serializer.data)

# >>> from rest_framework.renderers import JSONRenderer
# >>> from courses.models import Course
# >>> from courses.api.serializers import CourseSerializer
# >>> course = Course.objects.latest('id')
# >>> serializer = CourseSerializer(course)
# >>> JSONRenderer().render(serializer.data)