from django.urls import path
from .views import *

urlpatterns = [
    # User Management
    path('user/', UserApiView.as_view({'get': 'list', 'post': 'create'}), name='user_list_create'),
    path('user/<int:pk>/', UserApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user_detail'),

    # Parent Management
    path('parent/', ParentApiView.as_view({'get': 'list', 'post': 'create'}), name='parent_list_create'),
    path('parent/<int:pk>/', ParentApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='parent_detail'),

    # Student Management
    path('student/', StudentApiView.as_view({'get': 'list', 'post': 'create'}), name='student_list_create'),
    path('student/<int:pk>/', StudentApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='student_detail'),

    # Teacher Management
    path('teacher/', TeacherApiView.as_view({'get': 'list', 'post': 'create'}), name='teacher_list_create'),
    path('teacher/<int:pk>/', TeacherApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='teacher_detail'),

    # Class and Schedule Management
    path('class/', ClassApiView.as_view({'get': 'list', 'post': 'create'}), name='class_list_create'),
    path('class/<int:pk>/', ClassApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='class_detail'),

    # Academic Records Management
    path('academic-record/', AcademicRecordApiView.as_view({'get': 'list', 'post': 'create'}), name='academic_record_list_create'),
    path('academic-record/<int:pk>/', AcademicRecordApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='academic_record_detail'),

    # Attendance Management
    path('attendance/', AttendanceApiView.as_view({'get': 'list', 'post': 'create'}), name='attendance_list_create'),
    path('attendance/<int:pk>/', AttendanceApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='attendance_detail'),

    # Examination Management
    path('examination/', ExaminationApiView.as_view({'get': 'list', 'post': 'create'}), name='examination_list_create'),
    path('examination/<int:pk>/', ExaminationApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='examination_detail'),

    # Grade Management
    path('grade/', GradeApiView.as_view({'get': 'list', 'post': 'create'}), name='grade_list_create'),
    path('grade/<int:pk>/', GradeApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='grade_detail'),

    # Library Management (Books and Transactions)
    path('book/', BookApiView.as_view({'get': 'list', 'post': 'create'}), name='book_list_create'),
    path('book/<int:pk>/', BookApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book_detail'),

    path('book-transaction/', BookTransactionApiView.as_view({'get': 'list', 'post': 'create'}), name='book_transaction_list_create'),
    path('book-transaction/<int:pk>/', BookTransactionApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book_transaction_detail'),

    # Reports and Analytics
    path('report/', ReportViewSet.as_view(), name='report_list_create'),
    path('report/<int:pk>/', ReportDetailApiView.as_view(), name='report_detail'),

    # User Authentication (Login and Register)
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    
    # Group Management (Roles)
    path('groups/', group_list, name='group_list'),
]
