from django.contrib import admin

# Register your models here.
from .models import Board
from .models import Topic
from .models import Post

class display(admin.ModelAdmin):
    list_display = ['name','description']
admin.site.register(Board,display)

class displayTopic(admin.ModelAdmin):
    list_display = ['subject','board']
admin.site.register(Topic,displayTopic)


class displayPost(admin.ModelAdmin):
    list_display = ['message','topic']
admin.site.register(Post,displayPost)
