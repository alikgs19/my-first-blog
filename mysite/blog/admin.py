from django.contrib import admin

from .models import User , Post , Comment


class PostInline(admin.TabularInline):
	# def posttitle(self,obj)
	# def __str__(self)
    model = Post



class UserAdmin(admin.ModelAdmin):
	fieldsets = (
		('timeline' , 
				{
				'fields' : ( ('username', 'name') , 'family')
				}),
		('Advance' , 
			{
			'fields': ('birthdate',)
			}),
	)

	# readonly_fields = ('username',)
	inlines = [
		PostInline,
	]
	list_display = ('username', 'birthdate')
	list_filter = ('birthdate',)
# class UserAdmin(admin.ModelAdmin):
# 	exclude = ( 'birthdate',)
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
	# list_display = ('username', 'name', 'family')
	# list_filter = ['username']
    # inlines = [PostInline]
    # pass 
	# search_fields = ['question_text']
# @admin.register(User)
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
# 	pass 
# class UsearAdmn(admin.ModelAdmin):
# 	pass 
	
admin.site.register(User,UserAdmin)
# admin.site.register(Post)