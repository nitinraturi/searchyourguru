from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserCategoryInline(admin.StackedInline):
    model = UserCategory
    can_delete = False
    verbose_plural_name = "User Subjects"
    fk_name = 'user'


class UserLocationPreferenceInline(admin.StackedInline):
    model = UserLocationPreference
    can_delete = False
    verbose_plural_name = "User Location Preferences"
    fk_name = 'user'


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_plural_name = "User Profile"
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display_links = ['email']
    search_fields = ('email',)
    ordering = ('email',)
    inlines = (UserProfileInline, UserCategoryInline,
               UserLocationPreferenceInline)
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser',)
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'user_type')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'user_type')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'user_type')}
         ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class AllZipCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'zipcode', 'po_name', 'latitude',
                    'longitude', 'district', 'state', 'country')
    search_fields = ('zipcode',)
    list_display_links = ('id', 'zipcode', 'po_name')


admin.site.register(User, CustomUserAdmin)
admin.site.register(AllZipCode, AllZipCodeAdmin)
