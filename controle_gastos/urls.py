from django.contrib import admin
from django.urls import path
from contas.views import home, listagem, nova_transacao, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('', listagem, name='url_listagem'),
    path('nova/', nova_transacao, name='url_nova'),
    path('update/<int:pk>/', update, name='url_update'),
     path('delete/<int:pk>/', update, name='url_delete')
]
