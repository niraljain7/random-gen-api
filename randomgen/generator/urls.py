from django.urls import path
from .views import Randomgen

urlpatterns = [
	path("random/<int:num>", Randomgen.as_view(), name="random_gen"),
]