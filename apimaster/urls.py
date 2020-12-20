from django.urls import path
from . import views
urlpatterns = [
    path('api/deletePizza/<int:pk>',views.deletePizza,name='deletePizza'),
    path('api/createPizza',views.createPizza,name='createPizza'),
    path('api/listPizza',views.listPizza,name='listPizza'),
    path('api/filterBySize/<size>',views.filterBySize,name='filterBySize'),
    path('api/filterByType/<typeOfPizza>',views.filterByType,name='filterByType'),
    path('api/updatePizza/<int:pk>',views.updatePizza,name='updatePizza'),



]