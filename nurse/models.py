from django.db import models

# Create your models here.
class NURSE_DETAILS(models.Model):
    Nurse_id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=20)
    Super_id=models.ForeignKey(to='self',null=True,blank=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.Nurse_id)+'   '+self.Name

class NURSE_MONITOR(models.Model):
    Nid =  models.ForeignKey(NURSE_DETAILS,on_delete=models.CASCADE)
    Time = models.DateTimeField()
    Status = models.BooleanField(default=True,verbose_name='Is the Nurse Healthy')

    class Meta:
        unique_together = ('Nid','Time')