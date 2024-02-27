from django.urls import path
from . import views
urlpatterns=[
    path('',views.QuestionList.as_view()),
    path('<int:pk>/',views.QuestionDetail.as_view()),
    path('list/',views.list_q),
    path('list/<int:pk>/',views.list_detail),
    path('update/<int:pk>/',views.ques_upd),
    path('delete/<int:pk>/',views.QuestionDelete.as_view())


]   