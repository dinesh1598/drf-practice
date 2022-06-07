from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .models import Course
from .serializers import CourseSerializer,UserSerializer
from .permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def api_root(request,format=None):
    return Response(
        {
            'users':reverse('user-list',request=request,format=format),
            'course':reverse('course-list',request=request,format=format)
        }
    )

class CourseLst(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) 

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


