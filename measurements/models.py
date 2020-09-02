from django.db import models


# Create your models here.
class Area(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    longitude = models.FloatField()
    latitude = models.FloatField()

    @property
    def number_of_locations(self):
        return self.location_set.count()

    @property
    def average_measurement(self):
        sum = 0
        count = 0
        location_list = self.location_set.all()
        for location in location_list:
            measurement_list = location.measurement_set.all()
            for measurement in measurement_list:
                sum += measurement.value
                count += 1
        if count == 0:
            return None
        else:
            return sum / count

    def __str__(self):
        return str(self.name)


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    altitude = models.IntegerField()
    area = models.ForeignKey(Area, on_delete=False)

    def __str__(self):
        return str(self.area.name) + ":" + str(self.name)


class Measurement(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.FloatField()
    date = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=False)

    def __str__(self):
        return "measurement@" + str(self.location.name) + ":" + str(self.location.area.name)
