from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Nominee, Vote , Feedback

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('election_id',)}),
    )

class NomineeAdmin(admin.ModelAdmin):
    list_display = ('name', 'election_id', 'vote_count', 'vote_percentage')

    def vote_count(self, obj):
        return Vote.objects.filter(nominee=obj).count()

    def vote_percentage(self, obj):
        total_votes = Vote.objects.filter(election_id=obj.election_id).count()
        nominee_votes = Vote.objects.filter(nominee=obj).count()
        if total_votes == 0:
            return "0%"
        return f"{(nominee_votes / total_votes) * 100:.2f}%"

    vote_count.short_description = 'Vote Count'
    vote_percentage.short_description = 'Vote Percentage'

admin.site.register(Nominee, NomineeAdmin)
admin.site.register(Vote)
admin.site.register(CustomUser)
admin.site.register(Feedback)

