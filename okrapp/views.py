from django.shortcuts import render
from django.http import JsonResponse
from .models import Checklist, KJBGoal, KJBGoalType, KJBCategory, CategoryPoints, ChecklistTable

def sub_categories(request, checklist):

    data = {}

    kjb_goal_types= KJBGoalType.objects.filter(name=checklist)
    for kjb_goal_type in kjb_goal_types:
        kjb_goals = KJBGoal.objects.filter(goal_type=kjb_goal_type.id)
        for kjb_goal in kjb_goals:

            checklist_data = Checklist.objects.filter(plan_id=kjb_goal.kjb_category_id_id)
            if checklist_data:
                print(checklist_data[0].__dict__)
                data ['date'] = checklist_data[0].date
                data ['status'] = checklist_data[0].status


            kjb_category = KJBCategory.objects.get(id=kjb_goal.kjb_category_id_id)
            sub_categories =  CategoryPoints.objects.filter(category=kjb_category.id).values_list('name')
            data['sub_categories'] = [ sub_category for sub_category in sub_categories]

    # check_list_table = ChecklistTable.objects.filter(checklist=checklist)
    
    # checklist_table = Checklist.objects.filer(plan_id=)
    print(data)

    return JsonResponse(data)