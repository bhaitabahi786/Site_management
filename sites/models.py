from django.db import models

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
    manpower = models.ForeignKey(Manpower, on_delete=models.CASCADE)
    date = models.DateField()
    present_or_absent = models.TextChoices("PA","Present Absent")
    overtime = models.DecimalField(max_digits=20, decimal_places=2)
    amount_taken = models.DecimalField(max_digits=100, decimal_places=2)
    per_day_wages = models.DecimalField(max_digits=100, decimal_places=2)


class Expense(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField()



class Tool(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()




