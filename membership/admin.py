from django.contrib import admin
from .models import Membership, MembershipType


class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date',
        'full_name',
        'birth_date',
        'phone_number',
        'membership_type',
        'application_granted',
    )

    ordering = ('date',)


class MembershipTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Membership, MembershipAdmin)
admin.site.register(MembershipType, MembershipTypeAdmin)