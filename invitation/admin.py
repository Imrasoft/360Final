from django.contrib import admin
from .models import Invitation, FriendInvitation, SuggestedInvitee


class InvitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'organization', 'email', 'code', 'accepted', 'created_on', 'updated_on')
    list_filter = ['created_on']
    search_fields = ['name', 'email', 'organization']


class FriendInvitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'code', 'accepted', 'sender', 'created_on', 'updated_on')
    list_filter = ['created_on']
    search_fields = ['name', 'email', 'sender']


class SuggestedInviteeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'invitation_status', 'verification_status', 'doctor', 'created_on',
                    'updated_on')
    list_filter = ['created_on']
    search_fields = ['name', 'email', 'doctor']


admin.site.register(Invitation, InvitationAdmin)
admin.site.register(FriendInvitation, FriendInvitationAdmin)
admin.site.register(SuggestedInvitee, SuggestedInviteeAdmin)
