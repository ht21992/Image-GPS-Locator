from django.contrib import admin
from django.urls import path
from .views import main,upload_document
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main-page"),
    path('upload/', upload_document, name="upload-document")
]
