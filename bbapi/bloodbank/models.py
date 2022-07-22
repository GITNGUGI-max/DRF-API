from django.db import models

# Create your models here.
class County(models.Model):
	id=models.IntegerField(help_text='Enter count number', primary_key=True, null=False)
	countyName=models.TextField(help_text='Enter county name', default='')

	def __str__(self):
		return self.countyName
class SubCounty(models.Model):
	county=models.ForeignKey(County, on_delete=models.CASCADE,  null=False)
	subCountyName=models.TextField(help_text='Enter county name')

	def __str__(self):
		return self.subCountyName
class Donor(models.Model):
	donorName=models.CharField(max_length=250, help_text='Enter donor name')
	parentName=models.CharField(max_length=250, help_text='enter parent or guardian name')
	gender=models.CharField(max_length=100, help_text="Enter your sex")
	dateOfBirth=models.DateField('Date of Birth')
	bloodGroup=models.CharField( max_length=10, help_text='Enter your blood type')
	weight=models.IntegerField(help_text='enter weight in KGs')
	email=models.CharField(max_length=200, help_text='Enter an email address')
	location=models.CharField(max_length=200, help_text='Enter your current location')
	county=models.ForeignKey(County, on_delete=models.CASCADE,  default='', null=False, help_text='Enter your county of residence')
	subCounty=models.ForeignKey(SubCounty, on_delete=models.CASCADE, default='', null=False, help_text='Enter your county of residence')
	contactOne=models.IntegerField(help_text='Enter your contact number')
	contactTwo=models.IntegerField(help_text='Enter your contact number')
	voluntary=models.TextField( max_length=10,default='Yes')
	newDonor=models.CharField( max_length=10, default='Yes')
	lastDonated=models.DateField(null=True)
	image=models.ImageField(help_text='Attach your photo')
	# owner = models.ForeignKey('auth.User', null=True, default='', related_name='donors', on_delete=models.CASCADE)
	# DONOR_STATUS=(
	# 	(1, 'Active'),
	# 	(0, 'Inactive')
	# 	)
	# status=models.CharField(choices=DONOR_STATUS, max_length=10, default=0, help_text='DONOR STATUS')

	def __str__(self):
		return self.donorName

class Patient(models.Model):

	patientName=models.CharField(max_length=250, help_text='Enter patient name')
	hospital=models.CharField(max_length=250, default='', help_text='Enter hospital name')
	county=models.ForeignKey(County, on_delete=models.CASCADE,  default='', null=False, help_text='Enter your county of residence')
	subCounty=models.ForeignKey(SubCounty, on_delete=models.CASCADE, default='', null=False, help_text='Enter your county of residence')
	doctor=models.CharField(max_length=100, help_text='Enter your doctors name')
	contactName=models.CharField(max_length=100, help_text='Enter your contact name')
	email=models.CharField(max_length=200, help_text='Enter an email address')
	contactDate=models.DateField(auto_now_add=True)
	requiredDate=models.DateField(auto_now_add=True)
	bloodUnits=models.IntegerField(help_text='Enter amount of blood required')
	bloodGroup=models.CharField(max_length=10, help_text='Enter your blood type')
	contactOne=models.IntegerField( help_text='Enter your contact number')
	contactTwo=models.IntegerField( help_text='Enter your contact number')
	reason=models.TextField(help_text='Enter reason for requiring blood')
	# owner = models.ForeignKey('auth.User', default='', related_name='patients', on_delete=models.CASCADE)
	# PATIENT_STATUS=(
	# 	('1', 'Active'),
	# 	('0', 'Inactive')
	# 	)
	# status=models.CharField(choices=PATIENT_STATUS, max_length=10, default=0, help_text='PANICIENT STATUS')
	image=models.ImageField(help_text='Attach your photo')

class Message(models.Model):
	sender=models.CharField(max_length=10)
	senderName=models.TextField( help_text='Enter your contact number')
	senderEmail=models.CharField(max_length=200, help_text='Enter an email address')
	sentDate=models.DateField()
	contact=models.IntegerField()
	messsage=models.TextField(default='', help_text='Write your message here')
	MESSAGE_STATUS=(
		('r', 'Read'),
		('un', 'Unread'),
		)
	status=models.CharField(choices=MESSAGE_STATUS, max_length=10, default=0, help_text='MESSAGE_STATUS')




