from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import jatatawifi_stock_market

# Register your models here.
# class janataResource(resources.ModelResource):
#     class Meta:
#         model = jatatawifi_stock_market
    
   
    
      
class janataAdmin(ImportExportModelAdmin):
    pass

admin.site.register(jatatawifi_stock_market,janataAdmin)
