from django.urls import path
from . import views

urlpatterns = [
    path('<int:fileinfo_id>',views.file_info,name='file_info'),
    path('',views.fileinfo_all,name='fileinfo_all'),
]
