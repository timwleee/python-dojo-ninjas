from django.conf.urls import url, include # Notice we added include
from django.contrib import admin

urlpatterns = [
  url(r'^', include('apps.book_authors_app.urls'))
]
