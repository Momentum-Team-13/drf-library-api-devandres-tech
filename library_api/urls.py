from library_api import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('books/', views.BookListCreate.as_view()),
	path('books/<int:pk>', views.BookRetrieveUpdateDestroy.as_view()),
	path('books/<int:pk>/notes', views.BookNotesListCreate.as_view()),
	path('books/<int:pk>/notes/<int:note_pk>', views.BookNoteUpdate.as_view()),
	path('book-trackers/', views.BookTrackerListCreate.as_view()),
	path('book-trackers/<int:pk>', views.BookTrackerRetrieveUpdateDestroy.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
	path('auth/', include('djoser.urls')),
	path('auth/', include('djoser.urls.authtoken')),
]

# images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
