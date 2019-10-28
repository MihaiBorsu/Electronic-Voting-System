from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('evs/', views.index, name='evs'),
    path('<int:votingevent_id>/', views.voting_event_detail, name='voting_event_detail'),
    path('<int:votingevent_id>/<int:question_id>/', views.question_detail, name='question_detail'),
    path('<int:votingevent_id>/<int:question_id>/results/', views.result, name='results'),
    path('<int:votingevent_id>/<int:question_id>/vote/', views.vote, name='vote'),
]
