from django.urls import path
from . import views

urlpatterns = [
    path('', views.RentCreateListView.as_view(), name='rents'),
    path('<int:rent_id>/', views.RentDetailView.as_view(), name='rent_detail'),
    path('user/<int:user_id>/rents/',
         views.UserRentsView.as_view(), name='users_rents'),
    path('user/<int:user_id>/rents/<int:rent_id>/',
         views.UserRentDetail.as_view(), name='users_rents'),
]
