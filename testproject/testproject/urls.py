from django.contrib import admin
from django.urls import path, include
from printF.views import renderHomepage
urlpatterns = [
    path('', renderHomepage),
    path('admin/', admin.site.urls),
    path('app/', include('printF.urls'))
]
