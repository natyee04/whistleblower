from django.urls import path
from . import views

app_name = "history"
urlpatterns = [
path("case/<int:id>/", views.case, name="case"),
path("lookup/", views.lookup, name="lookup"),
]