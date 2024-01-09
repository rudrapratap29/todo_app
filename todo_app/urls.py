from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('task_list/', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
