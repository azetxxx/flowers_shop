from django.contrib import admin

from users.models import EmailVerification, User

# Register your models here.

admin.site.register(User)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
