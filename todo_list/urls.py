from django.urls import path

from todo_list.views import ListTodoAPIView, CreateTodoAPIView, UpdateTodoAPIView, DeleteTodoAPIView

app_name = 'todo_list'

urlpatterns = [
    path("", ListTodoAPIView.as_view(),name="todo_list"),
    path("create/", CreateTodoAPIView.as_view(),name="create_todo"),
    path("update/<int:pk>/", UpdateTodoAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/", DeleteTodoAPIView.as_view(),name="delete_todo"),
]