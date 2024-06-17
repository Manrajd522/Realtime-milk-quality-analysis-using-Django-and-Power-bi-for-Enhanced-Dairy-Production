from django.urls import path 
from .import views
urlpatterns=[
    path('user/',views.user,name='user'),
    path('record/',views.record,name='record'),
    path('total/',views.total,name='total'),
    path('', views.dashboard, name='dashboard'),
    path('get-monthly-collection-data/', views.get_monthly_collection_data, name='get_monthly_collection_data'),
    path('visuals/',views.visuals,name='visuals'),
    path('update/<int:record_id>/', views.update_record, name='update_record'),
    path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="login")
    
    
    
]