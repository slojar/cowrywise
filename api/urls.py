from django.urls import path
from .views import AnswerView

urlpatterns = [
    # Note to always append a trailing slash "/" at the when calling each endpoint
    path('', AnswerView.as_view(), name='answer'),
]
