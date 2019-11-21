from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('leitos/', views.LeitosListView.as_view(), name=None),
    path('leitos/<int:pk>', views.LeitosListView.as_view(), name=None),

]
