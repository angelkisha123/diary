from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage),
    path('add-member/', views.addMember, name='add-member'),
    path('view-member/',views.viewMember, name='view-member'),
    path('edit-member/<str:pk>/', views.editMember, name='edit-member'),
    path('delete-member/<str:pk>/', views.deleteMember, name='delete-member'),
    path('add-chapter',views.addChapter, name='addChapter'),
    path('chapter',views.viewChapter,name='viewChapter' ),
    path('modal',views.modal, name="modal"),
    path('edit-chapter', views.editChapter, name="editChapter"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)