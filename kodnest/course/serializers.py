from rest_framework import serializers
from django.contrib.auth.models import User
from course.models import Course,LANGUAGE_CHOICES,STYLE_CHOICES

class CourseSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model=Course
        fields=('id', 'title', 'code', 'linenos',
                  'language', 'style','owner', )

class UserSerializer(serializers.ModelSerializer):
     course=serializers.PrimaryKeyRelatedField(many=True,queryset=Course.objects.all())
     
     
     class Meta:
       model=User
       fields=('id','username','course')