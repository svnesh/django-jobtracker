from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('user/', views.UserPage, name='user-page'),
    
    path('client/<str:pk_test>', views.clients, name='client'),
    path('create_client', views.clientForm, name='create_client'),

    path('employee/', views.employee, name='employee'),
    path('account/', views.accountSettings, name='account'),
    path('create_employee/', views.employeeForm, name='create_employee'),
    path('update_employee/<str:pk>', views.updateEmployee, name='update_employee'),

    path('delete_function/<str:pk>/<str:myModel>', views.deleteFunction, name='delete_function'),

    path('project/', views.projects, name='project'),
    path('create_project/<str:pk>', views.projectForm, name='create_project'),
    path('update_project/<str:pk>', views.updateProject, name='update_project'),

    path('create_tracker/<str:pk>', views.trackerForm, name='create_tracker'),
    path('tracker/', views.tracker, name='tracker'),
]