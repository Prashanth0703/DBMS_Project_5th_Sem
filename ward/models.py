from django.db import models

# Create your models here.
class WARD_DETAILS(models.Model):
    Ward_No = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    Capacity = models.IntegerField(default=20)

    def __str__(self):
        return str(self.Ward_No)+'  '+self.Name

class DOCTOR_WORKS(models.Model):
    Ward_ID = models.ForeignKey(WARD_DETAILS,on_delete=models.CASCADE)
    Doc_ID = models.ForeignKey('doctor.DOCTOR_DETAILS',on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('Ward_ID', 'Doc_ID')
        verbose_name = "Doctor Working Ward"

class NURSE_WORKS(models.Model):
    Ward_ID = models.ForeignKey(WARD_DETAILS,on_delete=models.CASCADE)
    Nurse_ID = models.ForeignKey('nurse.NURSE_DETAILS',on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('Ward_ID', 'Nurse_ID')
        verbose_name = "Nurse working Ward"

class WARD_MANAGED_BY(models.Model):
    Ward_ID = models.ForeignKey(WARD_DETAILS,on_delete=models.CASCADE)
    MgrNurse_ID = models.ForeignKey('nurse.NURSE_DETAILS',on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('Ward_ID', 'MgrNurse_ID')
        verbose_name_plural = "Ward Managing Nurse"