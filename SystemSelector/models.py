from django.db import models


class System(models.Model):
    name = models.CharField(max_length=400, unique=True)
    taken = models.BooleanField()

    def __str__(self):
		return self.name


class Group(models.Model):
    project_system = models.ForeignKey(System, on_delete=models.SET_NULL)
    name = models.CharField(max_length=400)
    member_name_1 = models.CharField(max_length=200)
    member_name_2 = models.CharField(max_length=200)
    member_name_3 = models.CharField(max_length=200)
    member_name_4 = models.CharField(max_length=200)
    member_name_5 = models.CharField(max_length=200)


    def __str__(self):
        return self.name

