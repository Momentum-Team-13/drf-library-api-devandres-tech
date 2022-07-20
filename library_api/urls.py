from library_api import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('books/', views.BookListCreate.as_view()),
	path('books/<int:pk>', views.BookDetails.as_view()),
	path('books/<int:pk>', views.BookDestroy.as_view()),
	path('books/<int:pk>', views.BookUpdate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
