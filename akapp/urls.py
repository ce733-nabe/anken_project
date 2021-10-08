from django.urls import path
from . import views

app_name = 'akapp'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('anken/list/', views.AnkenListView.as_view(), name='anken_list'),
    path('anken/detail/<int:pk>/', views.AnkenDetailView.as_view(), name='anken_detail'),

    path('anken/create/', views.AnkenCreateView.as_view(), name='anken_create'),
    path('anken/create/complete/', views.AnkenCreateCompleteView.as_view(), name='anken_create_complete'),
    path('anken/update/<int:pk>/', views.AnkenUpdateView.as_view(), name='anken_update'),
    path('anken/delete/<int:pk>/', views.AnkenDeleteView.as_view(), name='anken_delete'),

    path('shuho/create/', views.ShuhoCreateView.as_view(), name='shuho_create'),
    path('shuho/create/complete/', views.ShuhoCreateCompleteView.as_view(), name='shuho_create_complete'),
    path('shuho/update/<int:pk>/', views.ShuhoUpdateView.as_view(), name='shuho_update'),
    path('shuho/delete/<int:pk>/', views.ShuhoDeleteView.as_view(), name='shuho_delete'),
    
]
