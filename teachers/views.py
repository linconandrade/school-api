from rest_framework import generics
from teachers.models import Teacher
from teachers.serializers import TeacherSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


class TeacherCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
