from django.contrib import admin

from chat.models import Chat, ChatRoom


class ChatAdmin(admin.ModelAdmin):
    list_display = ('author', 'room', 'body', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('author', 'room')
    date_hierarchy = 'created_on'
    ordering = ('created_on',)
    raw_id_fields = ('author',)


class ChatInLine(admin.TabularInline):
    model = Chat


class ChatRoomAdmin(admin.ModelAdmin):
    inlines = (ChatInLine, )
    model = ChatRoom
    list_display = ('name', 'active',)
    list_filter = ('active', 'created_on',)
    list_editable = ('active',)
    search_fields = ('name', 'participants',)
    raw_id_fields = ('participants',)
    date_hierarchy = 'created_on'
    ordering = ('active', 'created_on',)


admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Chat, ChatAdmin)
