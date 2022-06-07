from django.urls import  path

from course import views

urlpatterns=[
    path('course/',views.CourseLst.as_view(),name='course-list'),
    path('course/<int:pk>/',views.CourseDetail.as_view(),name='course-detail'),
    path('users/',views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/',views.UserDetail.as_view(),name='user-model'),
    path('',views.api_root),
]