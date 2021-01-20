from django.contrib import admin
from .models import Categoria
from .models import transacoes


admin.site.register(Categoria)
admin.site.register(transacoes)
# Register your models here.
