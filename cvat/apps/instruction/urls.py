from django.urls import path
from . import views

urlpatterns = [
    path('<int:tid>', views.InstructionView),
]

