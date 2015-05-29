from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_weight(weight):
	if weight < 60 or weight > 999:
		raise ValidationError("Invalid weight")

def validate_age(age):
	if age < 14 or age > 99:
		raise ValidationError("Invalid age")

def validate_height_ft(ft):
	if ft < 4 or ft > 7:
		raise ValidationError("Invalid height ft")

def validate_height_inch(inch):
	if inch < 0 or inch > 12:
		raise ValidationError("Invalid height inch")

def validate_positive(value):
	if value < 0:
		raise ValidationError("Invalid value")

class Food(models.Model):
	name = models.CharField(max_length = 30, default="food")
	calories = models.DecimalField(validators=[validate_positive], decimal_places=2, max_digits=10)
	fat = models.DecimalField(validators=[validate_positive], decimal_places=2, max_digits=10)
	carbs = models.DecimalField(validators=[validate_positive], decimal_places=2, max_digits=10)
	protein = models.DecimalField(validators=[validate_positive], decimal_places=2, max_digits=10)
	servingsize = models.CharField(default="1 serving", max_length=15)
	ourfood = models.BooleanField(default=False)
	ourfood2 = models.BooleanField(default=False)

	def __str__(self):
		return self.name

# class Meal(models.Model):
# 	foods = models.ManyToManyField(Food)
# 	summ = self.foods.aggregate(models.Sum('calories'))['calories__sum']

# 	@property
# 	def totalcals(self):
# 		sum = self.foods.aggregate(models.Sum('calories'))['calories__sum']
# 		if sum == None:
# 			return 0
# 		else:
# 			return sum

class MealPlan(models.Model):
	foods = models.ManyToManyField(Food, unique=False)
	owner = models.CharField(max_length=14, default= "")

	def __str__(self):
		return "mealplan of " + self.owner

	@property
	def totalcals(self):
		sum = self.foods.aggregate(models.Sum('calories'))['calories__sum']
		if sum == None:
			return 0
		else:
			return sum

	@property
	def totalfat(self):
	    sum = self.foods.aggregate(models.Sum('fat'))['fat__sum']
	    if sum == None:
	    	return 0
	    return sum

	@property
	def totalcarbs(self):
	    sum = self.foods.aggregate(models.Sum('carbs'))['carbs__sum']
	    if sum == None:
	    	return 0
	    return sum

	@property
	def totalprotein(self):
	    sum = self.foods.aggregate(models.Sum('protein'))['protein__sum']
	    if sum == None:
	    	return 0
	    return sum



class ExerciseBase(models.Model):
	name = models.CharField(max_length=40)
	met = models.DecimalField(validators=[validate_positive], max_digits=5, decimal_places=2)

	def __str__(self):
		return self.name


class UserExercise(models.Model):
	exercisebase = models.ForeignKey(ExerciseBase)
	duration = models.IntegerField(validators=[validate_positive], max_length=3)

	def __str__(self):
		return self.exercisebase.name + ' for ' + str(self.duration)


class ExercisePlan(models.Model):
	exercises = models.ManyToManyField(UserExercise, unique=False)
	owner = models.CharField(max_length=14, default="")


	def __str__(self):
		return "exercise plan of " + self.owner


class WeightExercise(models.Model):
	name = models.CharField(max_length=14, default= "weight exercise")
	weight = models.IntegerField(validators=[validate_positive], default=0)
	reps = models.IntegerField(validators=[validate_positive], default=0)
	sets = models.IntegerField(validators=[validate_positive], default=0)

	def __str__(self):
		return self.name

class WeightPlan(models.Model):
	weightExercises = models.ManyToManyField(WeightExercise, unique=False, null=True)
	owner = models.CharField(max_length=14, default="")
	workout_time = models.IntegerField(validators=[validate_positive], default=0)
	high_intensity = models.BooleanField(default=False)

	def __str__(self):
		return "weight plan of " + self.owner

	@property
	def intensity(self):
	    if self.high_intensity:
	    	return "High"
	    else:
	    	return "Moderate"


	


class UserProfile(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female')
		)
	user = models.OneToOneField(User, default=1)
	age = models.IntegerField(validators=[validate_age], default=18)
	gender = models.CharField(max_length=1, choices = GENDER_CHOICES, default='M')
	height_ft = models.IntegerField(validators=[validate_height_ft], default=5)
	height_inch = models.IntegerField(validators=[validate_height_inch], default=9)
	weight = models.IntegerField(validators=[validate_weight], default=150)
	calorie_goal = models.IntegerField(validators=[validate_positive], default=1500)
	mealplan = models.OneToOneField(MealPlan)
	exerciseplan = models.OneToOneField(ExercisePlan, null=True)
	loss_goal = models.IntegerField(validators=[validate_positive], default=0)
	weightplan = models.OneToOneField(WeightPlan, null=True)


	@property
	def cals_from_weights(self):
		return 0.023765 * self.weightplan.workout_time * self.weight



	@property
	def cals_from_exercise(self):
		sum = 0
		for ex in self.exerciseplan.exercises.all():
			calsburned = ((float(ex.exercisebase.met) * 3.5 * (self.weight/2.2046)/200)) * ex.duration
			sum = sum + calsburned
		return sum


	@property
	def deficit(self):
		return int(self.calorie_goal - self.mealplan.totalcals + int(self.cals_from_exercise) + int(self.cals_from_weights))

	@property
	def running_needed(self):
		if (self.deficit < 50):
			run = ExerciseBase.objects.get(id=9)
			met = run.met
			return int(float(self.deficit*-1)/(float(met) * 3.5 * ((float(self.weight)/2.2046)/200)))
		else:
			return 0

	@property
	def fat_recommendation(self):
		fat = self.mealplan.totalfat
		if fat > 75:
		    return True

		else:
		    return False


	@property
	def carbs_recommendation(self):
		carbs = self.mealplan.totalcarbs
		if carbs > 310:
		    return True
		else:
		    return False


	@property
	def protein_recommendation(self):
		protein = self.mealplan.totalprotein
		if protein < 50:
		    return "You are below your recommended daily protein intake. Consider eating one of our 'recommended' meals to reach your protein goal."
		    return True
		else:
			return False
			return "Your protein intake is within a healthy range!"




