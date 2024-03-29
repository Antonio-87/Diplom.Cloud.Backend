from django.urls import path

from .views import FileCreateView, FileDestroyView, FileUpdateView

urlpatterns = [
    path("files/", FileCreateView.as_view()),
    path("files/update/<int:pk>/", FileUpdateView.as_view()),
    path("files/delete/<int:pk>/", FileDestroyView.as_view()),
]