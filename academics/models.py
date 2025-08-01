from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class StudentNew(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

# 1 create()
# t1=Teacher.objects.create(name="Sir Adil" ,subject="AI")
# s1 = Student.objects.create(name="Aqil", roll_no="it5637", teacher=t1)
# 2 show all data
# students=Student.objects.all()
# >>> for s in students:
# ... print(s.name,s.roll_no)
# 3 COUNT 
# >>> Student.objects.filter(name="Aqil", roll_no="it5637").count()
# 4 get(),add,all
#c1 = Course.objects.get(code="mt001")      
# >>> c2 = Course.objects.get(code="isl90")
# >>> s.courses.add(c1, c2)
# >>> s.courses.all()
# first()
# student = Student.objects.filter(teacher__name="Sir Arslan").first()
# >>> print(student)
# 5 
# >>> Student.objects.last()
# <Student: Aqil>
# >>> Student.objects.first()
# <Student: Mohsin>
# >>> 6
# Student.objects.exclude(teacher__name="Sir Adil")
# <QuerySet [<Student: Mohsin>, <Student: Aqil>, <Student: Aqil>]>
# 7
#Course.objects.order_by("code")
# <QuerySet [<Course: Chemistry>, <Course: islamiat>, <Course: math>, <Course: Physics>]>
# >>> reverse
#Course.objects.order_by("-code")
# <QuerySet [<Course: Physics>, <Course: math>, <Course: islamiat>, <Course: Chemistry>]>
# >>> reverse 8
# Course.objects.order_by("code").reverse()
# <QuerySet [<Course: Physics>, <Course: math>, <Course: islamiat>, <Course: Chemistry>]>
# >>> 9 ,10
#Student.objects.values("name","roll_no")
# <QuerySet [{'name': 'Mohsin', 'roll_no': 'PUCIT-21'}, {'name': 'Aqil', 'roll_no': 'it5637'}, {'name': 'Aqil', 'roll_no': 'it5637'}]
#  Student.objects.values_list("name","roll_no", flat=True)
# <QuerySet ['PUCIT-21','it5637'),'it5637']>
#11 distinct()
# Student.objects.values("name").distinct()
# <QuerySet [{'name': 'Mohsin'}, {'name': 'Aqil'}]>

#12 union
# q1=Student.objects.values_list("name",flat=True) (again)
# >>> q2=Teacher.objects.values_list("name",flat=True)
# >>> q1.union(q2)
# <QuerySet ['Aqil', 'Mohsin', 'Sir Adil', 'Sir Ali', 'Sir Arslan']>
#13 q1.intersection(q2)
# <QuerySet []>
#14 Course.objects.filter(code="phy101").exists()
# True
## is null()
# >>> Student.objects.filter(teacher__isnull=True)
# <QuerySet []>
# select_related()
#>>> students=Student.objects.select_related("teacher").all()
# >>> for s in students:
# ...     print(s.name,s.teacher.name)
# ... 
# Mohsin Sir Arslan
# Aqil Sir Ali
# Aqil Sir Ali
# >>> prefetch_related()
#students = Student.objects.prefetch_related('courses').all() (subquery)
# >>> for s in students:
# ...     print(s.name)
# ...     for c in s.courses.all():
# ...         print("", c.title)
# load()
# Student.objects.only('name', 'roll_no')
# <QuerySet [<Student: Mohsin>, <Student: Aqil>, <Student: Aqil>]>
#defer()
#Student.objects.defer('teacher')
# <QuerySet [<Student: Mohsin>, <Student: Aqil>, <Student: Aqil>]>
#  get or create
# student, created = Student.objects.get_or_create(
# ...     roll_no="IT103",
# ...     defaults={"name": "Adil", "teacher": t}
# ... )
# >>> student.name
# 'Adil'
# >>> 
# >>> student.name
# 'Adil Khan'
# bulk_create
#Student.objects.bulk_create([
# ...     Student(name="Ali", roll_no="IT201", teacher=t),
# ...     Student(name="Sara", roll_no="IT202", teacher=t),
# ...     Student(name="Zain", roll_no="IT203", teacher=t),
# ... ])
# [<Student: Ali>, <Student: Sara>, <Student: Zain>]
# >>> 
# count()
# total = Student.objects.count()
# >>> print("Total students", total)
# Total students 8
# first(),last()
# Student.objects.filter(name="Aqil").first()
# <Student: Aqil>
# >>> Student.objects.filter(name="Aqil").last()
# <Student: Aqil>
# >>> exists()
#>>> Student.objects.filter(name="Mohsin").exists()
# True
# >>> Student.objects.filter(name="Mobeenn").exists()
# False
#contains()
# Student.objects.filter(name__contains="Ali")
# <QuerySet [<Student: Ali>]>
# delete()
# stud=Student.objects.get(id=1)
# >>> stud.delete()
# (3, {'academics.Student_courses': 2, 'academics.Student': 1})
# issue
# students = Student.objects.filter(roll_no__in=["IT201", "IT202"])
# >>> for s in students:
# ...     print(s.roll_no)
# greater and graete or equal
#Student.objects.filter(id__gt=5)
# <QuerySet [<Student: Ali>, <Student: Sara>, <Student: Zain>]>
# >>> Student.objects.filter(id__gte=2)
# <QuerySet [<Student: Aqil>, <Student: Aqil>, <Student: Aqil>, <Student: Adil Khan>, <Student: Ali>, <Student: Sara>, <Student: Zain>]>
# S
# >>> Student.objects.filter(id__lt=5)
# <QuerySet [<Student: Aqil>, <Student: Aqil>, <Student: Aqil>]>
# >>> startswith
# Student.objects.filter(name__startswith="A")
# <QuerySet [<Student: Aqil>, <Student: Aqil>, <Student: Aqil>, <Student: Adil Khan>, <Student: Ali>]>
# ends 
# >>> Student.objects.filter(name__endswith="A")
# <QuerySet [<Student: Sara>]>
# >>> 
# range()
#  Student.objects.filter(id__range=(3, 7))
# <QuerySet [<Student: Aqil>, <Student: Aqil>, <Student: Adil Khan>, <Student: Ali>, <Student: Sara>]>
#Student.objects.filter(teacher__isnull=True)
# <QuerySet []>
#
# Student.objects.annotate(course_count=Count('courses'))
# <QuerySet [<Student: Aqil>, <Student: Adil Khan>, <Student: Ali>, <Student: Sara>, <Student: Zain>, <Student: Aqil>, <Student: Aqil>]>
# >>> Student.objects.aggregate(min_age=Min('age'))
# {'min_age': 12}
# >>> Student.objects.aggregate(min_age=Max('age'))
# {'min_age': 56}
# >>> 
