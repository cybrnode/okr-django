from django.contrib import admin
from .models import KJBCategory, KJBGoalType, KJBGoal, Checklist, Reflection, CategoryPoints, ChecklistStatus, ChecklistTable



class KJBGoalAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        return readonly_fields + ('reflection_conclusion', 'reflection_plan')

    def reflection_conclusion(self, obj):
        # Return the value of the conclusion field from the related Reflection object
        return obj.plan_id.conclusion

    def reflection_plan(self, obj):
        # Return the value of the plan field from the related Reflection object
        return obj.plan_id.plan

    reflection_conclusion.short_description = 'Conclusion'  # Set custom column name in admin
    reflection_plan.short_description = 'Plan'  # Set custom column name in admin

    # Define the fields that should be editable
    fields = ('goal_type', 'plan_id', 'user_id', 'kjb_category_id', 'start_date', 'end_date', 'reflection_conclusion',
              'reflection_plan')


class ChecklistAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "category_points":
            kwargs["queryset"] = CategoryPoints.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def get_goal_type(self, obj):
        return obj.plan_id.goal_type

    def get_user_id(self, obj):
        return obj.plan_id.user_id

    def get_kjb_category_id(self, obj):
        return obj.plan_id.kjb_category_id

    def get_start_date(self, obj):
        return obj.plan_id.start_date

    def get_end_date(self, obj):
        return obj.plan_id.end_date

    def get_reflection_conclusion(self, obj):
        if obj.plan_id and obj.plan_id.plan_id:
            return obj.plan_id.plan_id.conclusion
        return ''

    def get_reflection_plan(self, obj):
        if obj.plan_id and obj.plan_id.plan_id:
            return obj.plan_id.plan_id.plan
        return ''

    list_display = (
        'plan_id', 'get_goal_type', 'get_user_id', 'get_kjb_category_id', 'get_start_date', 'get_end_date',
        'get_reflection_conclusion', 'get_reflection_plan'
    )

    # Set custom column names in admin
    get_goal_type.short_description = 'Goal type'
    get_user_id.short_description = 'User id'
    get_kjb_category_id.short_description = 'Kjb category id'
    get_start_date.short_description = 'Start date'
    get_end_date.short_description = 'End date'
    get_reflection_conclusion.short_description = 'Conclusion'
    get_reflection_plan.short_description = 'Plan'

    # Specify additional fields to display in read-only mode
    readonly_fields = (
        'get_goal_type',
        'get_user_id',
        'get_kjb_category_id',
        'get_start_date',
        'get_end_date',
        'get_reflection_conclusion',
        'get_reflection_plan'
    )
    
    

class CategoryPointsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('category',)


class ChecklistStatusAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'checklist',
        'category_points_with_category',
        'date',
        'status',
        'comment'
    )  # Include 'comment' in list_display
    
    list_filter = ('date', 'status', 'category_points')
    search_fields = ['checklist__id', 'category_points__id']
    date_hierarchy = 'date'

    def category_points_with_category(self, obj):
        return f"{obj.category_points.category.name} - {obj.category_points.name}"

    category_points_with_category.short_description = 'Category Points'
    class Media:
        js = (
            'js/admin.js',   # inside app static folder
        )


class ReflectionAdmin(admin.ModelAdmin):
    list_display = ('plan_id', 'date', 'conclusion', 'plan')
    list_filter = ('plan_id', 'date', 'conclusion', 'plan')
    search_fields = ['plan_id']
    date_hierarchy = 'date'

class ChecklistTableAdmin(admin.ModelAdmin):
    list_display = ('checklist',)
    # list_filter = ('plan_id', 'date', 'conclusion', 'plan')
    # search_fields = ['plan_id']
    # date_hierarchy = 'date'
    class Media:
        js = (
            'js/admin_checklist.js',   # inside app static folder
        )



admin.site.register(ChecklistStatus, ChecklistStatusAdmin)
admin.site.register(CategoryPoints, CategoryPointsAdmin)
admin.site.register(KJBCategory)
admin.site.register(KJBGoalType)
admin.site.register(KJBGoal, KJBGoalAdmin)
admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(Reflection, ReflectionAdmin)
admin.site.register(ChecklistTable, ChecklistTableAdmin)