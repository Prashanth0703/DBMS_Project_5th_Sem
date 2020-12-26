from django.db import models

# Create your models here.
class DOCTOR_DETAILS(models.Model):
    Dr_id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=20)
    Designation=models.CharField(max_length=20)
    Super_id=models.ForeignKey(to='self',null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name


class DOCTOR_MONITOR(models.Model):
    Drid =  models.ForeignKey(DOCTOR_DETAILS,on_delete=models.CASCADE)
    Time = models.DateTimeField()
    Status = models.BooleanField(default=True,verbose_name='Is the Doctor Healthy')
    class Meta:
        unique_together = ('Drid','Time')
        