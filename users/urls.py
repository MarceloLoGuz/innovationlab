from django.urls import path
from users import views

urlpatterns = [
    # MyUserClass
    path('signup', views.MyUserClass.as_view(), name='signup_user'),
    path('update/<int:id>/', views.MyUserClass.as_view(), name='update_user'),
    path('delete/<int:id>/', views.MyUserClass.as_view(), name='delete_user'),
    path('download-pdf', views.MyUserClass.as_view(), name='download_users_pdf'),
    # MyUserFilters
    path('filters', views.MyUserFilters.as_view(), name='filters'),
]