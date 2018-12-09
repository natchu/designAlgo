from django.db import models

class RawData(models.Model):
    X=0
    Y=1
    FLOW = ((X,'Consume'),(Y,'Generate'))
    read_timestamp = models.DateTimeField()
    interval_read = models.DecimalField(max_digits=5,decimal_places=3)
    energy_flow_direction = models.IntegerField(choices=FLOW)
    icp_id = models.PositiveIntegerField()

