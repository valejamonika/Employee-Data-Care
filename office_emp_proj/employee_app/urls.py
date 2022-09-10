from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('all_emp',views.all_emp,name='all_emp'),
    path('add_emp',views.add_emp,name='add_emp'),
    path('rem_emp',views.rem_emp,name='rem_emp'),
    path('filter_emp',views.filter_emp,name='filter_emp'),
    path('add',views.add,name='add'),
    path('remove/<int:emp_id>',views.remove,name='remove'),
    path('dept',views.dept,name='dept'),
    path('role',views.role,name='role'),
    
]