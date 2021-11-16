from django.urls import path, include
# from django.urls.conf import include
from .views import Owner_informationView,Dog_informationView
urlpatterns = [
    path("",Owner_informationView.as_view()),
    path("/dog",Dog_informationView.as_view())
]
