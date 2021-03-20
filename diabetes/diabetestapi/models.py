from django.db import models

class Diabetes(models.Model):
	name = models.CharField(max_length=20)
	pregnancies = models.CharField(max_length=20)
	glucose = models.CharField(max_length=20)
	blood_pressure = models.CharField(max_length=20)
	skin_thickness = models.CharField(max_length=20)
	insulin = models.CharField(max_length=20)
	bmi = models.CharField(max_length=20)
	diabetes_pedigree_function = models.CharField(max_length=20)
	age = models.CharField(max_length=20)

	def __str__(self):
		return self.name, pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age