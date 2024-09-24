from rest_framework import viewsets, permissions
from rest_framework import generics
from .models import User,Parent , Student, Teacher, Class, AcademicRecord, Attendance, Examination, Grade, Book, BookTransaction, Report
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
from .permissions import CustomPermission

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def group_list(request):
    group_objs = Group.objects.all()
    serializer = GroupSerializer(group_objs, many=True)
    return Response(serializer.data)

# User Authentication
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    password = request.data.get('password')
    hash_password = make_password(password) #encrypting the password
    request.data['password'] = hash_password #overriding value in password field

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Registration Successful')
    return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response('Invalid Credentials')
    
class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]

class ParentApiView(viewsets.ModelViewSet):
    queryset =Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]
    filterset_fields = ['name']
    search_fields = ['name']

class StudentApiView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]
    filterset_fields = ['name']
    search_fields = ['name']

class TeacherApiView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]
    filterset_fields = ['teacher_name', 'availability']
    search_fields = ['teacher_name']

class ClassApiView(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]

class AcademicRecordApiView(viewsets.ModelViewSet):
    queryset = AcademicRecord.objects.all()
    serializer_class = AcademicRecordSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]

class AttendanceApiView(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]

class ExaminationApiView(viewsets.ModelViewSet):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]

class GradeApiView(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]

class BookApiView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]

class BookTransactionApiView(viewsets.ModelViewSet):
    queryset = BookTransaction.objects.all()
    serializer_class = BookTransactionSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]

class ReportViewSet(generics.GenericAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]
    filterset_fields = ['report_name']
    search_fields = ['report_name']

    def get(self, request):

        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        
        return Response(serializer.data)

    def post(self, request):

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("Report Created")
        else:
            return Response(serializer.errors)

class ReportDetailApiView(generics.GenericAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]

    def get(self, request, pk):

        queryset = self.get_object()
        serializer = self.serializer_class(queryset)

        return Response(serializer.data)
    
    def put(self, request, pk):
        queryset = self.get_object()
        serializer = self.serializer_class(queryset, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response("Report Updated")
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        queryset = self.get_object()
        queryset.delete()
        return Response('Report Removed')   