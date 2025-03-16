from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# List all students
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

# View student details
class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'

# Create a new student
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, "Student added successfully!")
        return super().form_valid(form)

# Update student details
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, "Student updated successfully!")
        return super().form_valid(form)

# Delete a student
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Student deleted successfully!")
        return super().delete(request, *args, **kwargs)
