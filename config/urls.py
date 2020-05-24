from django.urls import path, include

urlpatterns = [
  # path('admin/', admin.site.urls),
    path('accounts', include('accounts.urls')),
    path('comment', include('comment.urls')),
    
]
