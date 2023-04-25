from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # 추가로 등록할 수 있는 

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('생성일', {'fields': ['pub_data'], 'classes':['collapse']}),
        ('질문 섹션', {'fields': ['question_text']})
    ]
    list_display = ('question_text', 'pub_data', 'was_published_recently')
    readonly_fields = ['pub_data']
    inlines = [ChoiceInline]
    list_filter = ['pub_data']
    search_fields = ['question_text', 'choice__choice_text']

admin.site.register(Question, QuestionAdmin)