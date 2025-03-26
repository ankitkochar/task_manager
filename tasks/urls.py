from django.urls import path
from .views import CreateTaskView, AssignTaskView, UserTasksView, GetUserDetailsView, CreateUserView

urlpatterns = [
    path('tasks/', CreateTaskView.as_view(), name='create_task'),
    path('tasks/<int:task_id>/assign/', AssignTaskView.as_view(), name='assign_task'),
    path('users/<int:user_id>/tasks/', UserTasksView.as_view(), name='user_tasks'),
    path('users/<int:user_id>/', GetUserDetailsView.as_view(), name='get_user_details'),
    path('users/', CreateUserView.as_view(), name='create_user'),
]
