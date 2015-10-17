from django.contrib import admin

from . models import Answer, Question

# Register your models here.

"""
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3
"""

"""

class ChoiceInLine(admin.TabularInline):
    model = Answer
    extra = 3
"""


"""

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]

"""


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']



admin.site.register(Answer)


#admin.site.register(Question, Answer, QuestionAdmin)



