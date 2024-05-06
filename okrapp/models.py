import logging
import sys
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey

from django.dispatch import receiver
from django.db.models.signals import post_save


class KJBCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class KJBGoalType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class KJBGoal(models.Model):
    goal_type = models.ForeignKey(KJBGoalType, on_delete=models.CASCADE)
    plan_id = models.ForeignKey('Reflection', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    kjb_category_id = models.ForeignKey(KJBCategory, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return str(self.goal_type)


class Checklist(models.Model):
    plan_id = models.ForeignKey(KJBGoal, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField()

    def __str__(self) -> str:
        return str(self.plan_id.goal_type)


class Reflection(models.Model):
    plan_id = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    date = models.DateField()
    what_did = models.TextField()
    what_like = models.TextField()
    what_not_like = models.TextField()
    what_improve = models.TextField()
    improve_reasons = models.TextField()
    conclusion = models.TextField()
    plan = models.TextField()


class CategoryPoints(models.Model):
    category = models.ForeignKey(KJBCategory, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name


class ChecklistStatus(models.Model):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    category_points = models.ForeignKey(
        CategoryPoints, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)  # Add the comment field

    def __str__(self):
        return self.comment


class Demo(models.Model):
    name = models.TextField()

    def __str__(self):
        return str(self.id)


class SubCategory(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class ChecklistTable(models.Model):
    date = models.DateField()
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    
    sub_cat = models.ForeignKey(
        CategoryPoints,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(KJBCategory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


logger = logging.getLogger(__name__)


@receiver(post_save, sender=Checklist)
def create_b_for_a(sender, instance: Checklist, created, **kwargs):
    print("Hello")

    if created == True:  # Check if A was created (not updated)

        try:
            
            print(instance)

            checklist_table =ChecklistTable.objects.create(
                checklist=instance,
                category=KJBCategory.objects.first(),
                category_points_id=CategoryPoints.objects.first()
            )

        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(f"An exception of type {exc_type.__name__} occurred: {exc_value}")

