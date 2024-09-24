from django.db import models
from django.contrib.auth.models import AbstractUser

# User model with roles
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    ]
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=300, unique=True)
    password = models.CharField(max_length=300)
    contact = models.BigIntegerField(null=True)
    location = models.CharField(max_length=300, null=True)
    image = models.ImageField(null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']

# Parent model
class Parent(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    students = models.ManyToManyField('Student', related_name='parent_set')

# Student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    enrollment_date = models.DateField()
    contact_info = models.CharField(max_length=15, blank=True, null=True)
    academic_records = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='student_set')
    relationship = models.CharField(max_length=100)
    
# Teacher model
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    hire_date = models.DateField()
    contact_info = models.CharField(max_length=255)
    availability = models.TextField(blank=True)

# Class model
class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')
    schedule = models.TextField()
    enrolled_students = models.ManyToManyField(Student, related_name='classes', blank=True)

# Academic Record model
class AcademicRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='academic_records_set')  # Changed related_name
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    year = models.IntegerField()

# Attendance model
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    class_attended = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=(('present', 'Present'), ('absent', 'Absent')))

# Examination model
class Examination(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    classes = models.ManyToManyField(Class, related_name='examinations')

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE, related_name='grades')
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)

# Library models
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    inventory_count = models.PositiveIntegerField()

class BookTransaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transactions')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

# Optional Report model for storing reports
class Report(models.Model):
    report_name = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    generated_by = models.ForeignKey(User, on_delete=models.CASCADE)
