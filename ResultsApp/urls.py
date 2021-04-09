from django.urls import path
from .views import index, add, editstudent, student_delete

urlpatterns = [
    path('', index, name='home'),
    path('addstudent',add, name='addstudent'),
    path('editstudent/<int:id>',editstudent,name='editstudent'),
    path('delete/<int:id>', student_delete, name='delete'),
]