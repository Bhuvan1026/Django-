from django.contrib import admin
from django.urls import path, include
# from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', RedirectView.as_view(url='counter', permanent=False)),  # Redirect root to /counter
    path('', include("counter.urls")),  # Replace yourappname with your actual app name
]