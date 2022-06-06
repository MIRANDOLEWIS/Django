from django.urls import path
from urlapp import views

urlpatterns = [
    path("",views.urlform,name = "urlform"),
    path("create",views.create,name="create"),
    path("<str:pk>",views.go,name="go")

]