

from django.contrib import admin
from apps.user_operation.models import GoodsFar

class GoodsFavAdmin(object):
    list_display = ['user','goods','id']




import xadmin
xadmin.site.register(GoodsFar,GoodsFavAdmin)