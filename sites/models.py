from django.db import models
from decimal import Decimal


class Site(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    quotation_amount = models.DecimalField(max_digits=50, decimal_places=2)


class Manpower(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    adhaarno = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)

class Attendance(models.Model):
    MAN_CHOICES = [("Present", "Present"), ("Absent", "Absent")]
    manpower = models.ForeignKey(Manpower, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    present_or_absent = models.CharField(max_length=10, choices=MAN_CHOICES)
    overtime = models.DecimalField(max_digits=20, decimal_places=2)
    amount_taken = models.DecimalField(max_digits=100, decimal_places=2)
    per_day_wages = models.DecimalField(max_digits=100, decimal_places=2)
    total_wages = models.DecimalField(max_digits=100, decimal_places=2,default=0)

    def calculate_total_wages(self):
        try:
            per_day_wages = Decimal(self.per_day_wages)
            amount_taken = Decimal(self.amount_taken)
            total_wages = per_day_wages - amount_taken
            return total_wages
        except Decimal.InvalidOperation:
            return Decimal(0)

    def save(self, *args, **kwargs):
        try:
            self.total_wages = Decimal(self.per_day_wages) - Decimal(self.amount_taken)
        except Decimal.InvalidOperation:
            self.total_wages = Decimal(0)
        super().save(*args, **kwargs)



class Expense(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField()

class Tool(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=100, decimal_places=2)

class total_amount_per_laborer(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    Manpower = models.ForeignKey(Manpower, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2)


class TotalSitesExpenseAmount(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    total_expense_amount = models.DecimalField(max_digits=100, decimal_places=2)

class TotalSitesToolAmount(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    total_tool_amount = models.DecimalField(max_digits=100, decimal_places=2)




