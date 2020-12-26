from django.db import models
from django.db.models import Q
from django.core.validators import MinLengthValidator

# Create your models here.
Male='Male'
Female='Female'
Other='Other'
Cheque,Cash,CC,DC,UPI,Insurance,Net_Banking= 'Cheque','Cash','CC','DC','UPI','Isurance','Net_Banking'
#Successful,Unsuccessful = 'Successful','Unsuccessful'
gender_choices=[(Male,'Male'),(Female,'Female'),(Other,'Other')]
Priority_Choices = [(1,'1-Low'),(2,'2'),(3,'3'),(4,'4'),(5,'5-High')]
MOP_Choices = [(Cheque,'Cheque'),(Cash,'Cash'),(CC,'Credit Card'),(DC,'Debit Card'),(UPI,'UPI'),(Insurance,'Insurance'),(Net_Banking,'Net Banking')]
Payment_Status = [('Successful','Successful'),('Unsuccessful','Unsuccessful')]

# Create your models here.
class PATIENT_DETAILS(models.Model):
    P_id=models.IntegerField(primary_key=True, unique=True)
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=6,choices=gender_choices,default='Male')
    City=models.CharField(max_length=20,default='Null')
    Street=models.CharField(max_length=20,default='Null')
    Pincode=models.IntegerField(default=0)
    Symptomatic=models.BooleanField(default=False)
    Previous_Disease=models.CharField(max_length=20,default='Null')
    Still_Exists=models.BooleanField(default=False)

    def __str__(self):
        return str(self.P_id)+"  "+self.Name
    class Meta:
        db_table = 'PATIENT_DETAILS'
        constraints = [
            models.CheckConstraint(
                check=Q(Age__gte=1), name='Pat_Age_gte_1'),

            models.CheckConstraint(
                check=Q(Age__lte=120), name='Pat_Age_lte_120'),
       ]

class DEPENDENT(models.Model):
    Patient_id = models.ForeignKey(PATIENT_DETAILS,on_delete=models.CASCADE)
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=6,choices=gender_choices,default='Male')

    class Meta:
        unique_together= ('Patient_id','Name')
        constraints = [
            models.CheckConstraint(
                check=Q(Age__gte=1), name='Dep_Age_gte_1'),
            
            models.CheckConstraint(
                check=Q(Age__lte=120), name='Dep_Age_lte_120'),
        ]
                 
class ADMITTED_TO(models.Model):
    Pat_ID = models.ForeignKey(PATIENT_DETAILS,primary_key=True,on_delete=models.CASCADE)
    Ward_ID = models.ForeignKey('ward.WARD_DETAILS',on_delete=models.CASCADE)
    Priority = models.IntegerField(choices=Priority_Choices,default=1)
    Health_Score =models.IntegerField()



    class Meta:
        db_table = 'ADMITTED_TO'
        constraints = [
            models.CheckConstraint(
                check=Q(Health_Score__gte=1),name='Health_Score_gte_1'),
            models.CheckConstraint(
                check=Q(Health_Score__lte=100), name='Health_Score_lte_100'),
        ]

# class HAS_DEPENDENT(models.Model):
#     Patient_ID = models.ForeignKey(PATIENT_DETAILS,on_delete=models.CASCADE)
#     Dep_Name = models.CharField(max_length=20)
    
    # class Meta:
    #     unique_together = ('Patient_ID', 'Dep_Name')
    #     verbose_name_plural = "Has Dependent"


class DEP_MONITOR(models.Model):
    Dep_id =  models.ForeignKey(PATIENT_DETAILS,on_delete=models.CASCADE)
    Time = models.DateTimeField()
    Status = models.BooleanField(default=True,verbose_name='Is the Dependent Healthy')

    class Meta:
        unique_together = ('Dep_id','Time')
        verbose_name_plural = 'Dependent Monitor'


class DECISION_MAKING(models.Model):
    Pid = models.OneToOneField(PATIENT_DETAILS,unique=True,on_delete=models.CASCADE)
    Diagnosis = models.BooleanField(default=False)
    Diag_Time = models.IntegerField(default=5, verbose_name='Time required for diagnosis (In mins)')
    Hospital_Recom = models.BooleanField(default=False)
    Patient_Dec = models.BooleanField(default=False)
    

class HOME_QUARANTINE_MONITOR(models.Model):
    Pat_ID =models.OneToOneField(PATIENT_DETAILS,unique=True,on_delete=models.CASCADE)
    Health_Status= models.CharField(max_length=50)
    Movements = models.BooleanField()
    class Meta:
        db_table = 'HOME_QUARANTINE_MONITOR'

class PAYMENT(models.Model):
    Patient_id = models.ForeignKey(PATIENT_DETAILS,on_delete=models.CASCADE)
    Bill_ID = models.IntegerField()
    Mode_of_Payment = models.CharField(max_length=11,choices=MOP_Choices)
    Status = models.CharField(max_length=12,choices=Payment_Status,default='Unsuccessful')

    class Meta:
        unique_together = ('Patient_id','Bill_ID')


class HAS_BANK(models.Model):
    Patient_id =models.ForeignKey(PATIENT_DETAILS,on_delete=models.CASCADE)
    Bank_Name= models.CharField(max_length=20)
    IFSC = models.CharField(max_length=11,validators=[MinLengthValidator(11,message='Enter IFSC code')])
    Account_No =models.CharField(max_length=20)
    Cheque_no = models.CharField(max_length=6,blank=True,null=True,validators=[MinLengthValidator(6,message='Enter 6 digit cheeque number')])
    Eligibility = models.BooleanField('Eligible')

    class Meta:
        unique_together = ('Patient_id','IFSC','Account_No')

class HAS_INSURANCE(models.Model):
    Patient_id =models.ForeignKey(PATIENT_DETAILS,on_delete=models.CASCADE)
    Insurance_Provider = models.CharField(max_length=20)
    Eligibility = models.BooleanField('Eligible')