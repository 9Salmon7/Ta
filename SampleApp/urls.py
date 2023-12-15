from django.urls import path
from .views import IndexView, P1View

urlpatterns = [
	path('', IndexView.as_view()),
	path('P1/', P1View.as_view()),
]