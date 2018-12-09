from django.db import models

class RawData(models.Model):
    X=0
    Y=1
    FLOW = ((X,'Consume'),(Y,'Generate'))
    read_timestamp = models.DateTimeField()
    interval_read = models.DecimalField(max_digits=5,decimal_places=3)
    energy_flow_direction = models.IntegerField(choices=FLOW)
    icp_id = models.PositiveIntegerField()

class AggregatedData(models.Model):
    BUYER = "buyer"
    SELLER = "seller"
    ROLE = ((BUYER,"Buyer"),(SELLER,"Seller"))
    icp_id = models.PositiveIntegerField()
    matched_amount = models.DecimalField(max_digits=6,decimal_places=4)
    read_date = models.DateField()
    read_time = models.TimeField()
    publish_datetime = models.DateTimeField()
    buyer_seller = models.CharField(choices=ROLE,max_length=7)
