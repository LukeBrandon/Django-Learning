from django.urls import include, path
from . import views

app_name = "polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #ex: /polls/2/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #ex: /polls/2/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #ex: /polls/2/vote
    path('<int:pk>/vote/', views.vote, name='vote'),
]
