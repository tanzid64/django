from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.AddMusicianView.as_view(), name='add_musician'),
    path('edit/<int:pk>', views.EditMusicianView.as_view(), name='edit_musician'),
    path('delete/<int:pk>', views.DeleteMusicianView.as_view(), name='delete_musician'),
]
