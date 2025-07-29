from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import Student

class StudentListView(LoginRequiredMixin, View):
    def get(self, request):
        students = Student.objects.filter(user=request.user)
        return render(request, 'student_list.html', {'students': students})

class StudentCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'student_form.html')

    def post(self, request):
        Student.objects.create(
            user=request.user,
            name=request.POST['name'],
            age=request.POST['age'],

        )
        return redirect('student-list')
# need 
class StudentUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        student = Student.objects.filter(id=id, user=request.user).first()
        if student:
            return render(request, 'student_form.html', {'student': student})
        return redirect('student-list')  

    def post(self, request, id):
        student = Student.objects.filter(id=id, user=request.user).first()
        if student:
            student.name = request.POST['name']
            student.age = request.POST['age']
            student.save()
        return redirect('student-list')


class StudentDeleteView(LoginRequiredMixin, View):
    def post(self, request, id):
        student = Student.objects.filter(id=id, user=request.user).first()
        if student:
            student.delete()
        return redirect('student-list')

