from django.urls import path
from . import views

app_name = "shared"
urlpatterns = [
    path("", views.home, name="home"),
    path("admin/reports", views.admin_report_list, name="admin_report_list"),
    path("upload_test", views.upload_test, name="upload_test"),
    path("view_files", views.view_files, name="view_files")
]
