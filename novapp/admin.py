from django.contrib import admin
from novapp.models import Member, UploadedDocument, Contact

# Register your models here.
admin.site.register(Contact)
admin.site.register(Member)
admin.site.register(UploadedDocument)
