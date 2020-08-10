from rest_framework import serializers

# We do not actually need serializers for this demonstration. They are only here to demonstrate their use.

#-------------------------------------------------------------------------------
class SerializerMinimum(serializers.Serializer): minimum = serializers.FloatField()
class SerializerMaximum(serializers.Serializer): maximum = serializers.FloatField()
class SerializerAverage(serializers.Serializer): average = serializers.FloatField()
class SerializerMedian (serializers.Serializer): median  = serializers.FloatField()

class SerializerAll(serializers.Serializer):
    minimum = serializers.FloatField()
    maximum = serializers.FloatField()
    average = serializers.FloatField()
    median  = serializers.FloatField()

#-------------------------------------------------------------------------------
class SerializerTemperatureMinimum(serializers.Serializer): temperature = SerializerMinimum()
class SerializerTemperatureMaximum(serializers.Serializer): temperature = SerializerMaximum()
class SerializerTemperatureAverage(serializers.Serializer): temperature = SerializerAverage()
class SerializerTemperatureMedian (serializers.Serializer): temperature = SerializerMedian()
class SerializerTemperatureAll    (serializers.Serializer): temperature = SerializerAll()

#-------------------------------------------------------------------------------
class SerializerHumidityMinimum(serializers.Serializer): humidity = SerializerMinimum()
class SerializerHumidityMaximum(serializers.Serializer): humidity = SerializerMaximum()
class SerializerHumidityAverage(serializers.Serializer): humidity = SerializerAverage()
class SerializerHumidityMedian (serializers.Serializer): humidity = SerializerMedian()
class SerializerHumidityAll    (serializers.Serializer): humidity = SerializerAll()

#-------------------------------------------------------------------------------
class SerializerTempAndHumidity(serializers.Serializer):
    temperature = SerializerAll()
    humidity    = SerializerAll()

#-------------------------------------------------------------------------------
class SerializerError(serializers.Serializer):
    error = serializers.CharField(max_length=256)