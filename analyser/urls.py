from django.urls import path
from . import views

urlpatterns = [
    path('samples/list', views.sample_list, name='all_samples'),
    path('samples/add', views.create_sample, name='process_image'),
    path('samples/<int:sample_id>/analyze/', views.analyze_sample, name='analyze-strip'),
]