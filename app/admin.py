from django.contrib import admin
from .models import Games, News, NewsPhoto, BackgroundPhoto, Document, DocumentCategory


admin.site.register(Games)
admin.site.register(News)
admin.site.register(NewsPhoto)
admin.site.register(BackgroundPhoto)
admin.site.register(Document)
admin.site.register(DocumentCategory)
