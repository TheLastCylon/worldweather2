import json
from django.http             import HttpResponse
from django.shortcuts        import render
from django.views.generic    import View
from rest_framework          import views
from rest_framework.response import Response

from .serializers import * # Technically, this demonstration does not require the use of serializers. They are only here to demonstrate their use.
from .validations import *
from .retriever   import Retriever
from .analyzer    import Analyzer

class TemperatureMinimum(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            temperature = Retriever('7856d02822474b99b99155147202807').get_analyzer(city, date_start, date_end).temperature_min()
            data        = { 'temperature': {"minimum": temperature} }
            results     = SerializerTemperatureMinimum(data, many=False).data
            return Response(results)
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)

class TemperatureMaximum(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            temperature = Retriever('7856d02822474b99b99155147202807').get_analyzer(city, date_start, date_end).temperature_max()
            data        = { 'temperature': {"maximum": temperature} }
            results     = SerializerTemperatureMaximum(data, many=False).data
            return Response(results)
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)

class TemperatureAverage(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            temperature = Retriever('7856d02822474b99b99155147202807').get_analyzer(city, date_start, date_end).temperature_average()
            data        = { 'temperature': {"average": temperature} }
            results     = SerializerTemperatureAverage(data, many=False).data
            return Response(results)
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)

class TemperatureMedian(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            temperature = Retriever('7856d02822474b99b99155147202807').get_analyzer(city, date_start, date_end).temperature_median()
            data        = { 'temperature': {"median": temperature} }
            results     = SerializerTemperatureMedian(data, many=False).data
            return Response(results)
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)

class TemperatureAll(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            analyzer = Retriever('7856d02822474b99b99155147202807').get_analyzer(city, date_start, date_end)
            data     = { 'temperature': {
                "minimum" : analyzer.temperature_min    (),
                "maximum" : analyzer.temperature_max    (),
                "average" : analyzer.temperature_average(),
                "median"  : analyzer.temperature_median ()} }
            results     = SerializerTemperatureAll(data, many=False).data
            return Response(results)
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)

class HumidityMinimum(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            humidity = Retriever('7856d02822474b99b99155147202807').get_analyzer(city, date_start, date_end).humidity_min()
            data        = { 'humidity': {"minimum": humidity} }
            results     = SerializerHumidityMinimum(data, many=False).data
            return Response(results)
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)

class HumidityMaximum(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            humidity = Retriever('7856d02822474b99b99155147202807').get_analyzer(city, date_start, date_end).humidity_max()
            data        = { 'humidity': {"maximum": humidity} }
            results     = SerializerHumidityMaximum(data, many=False).data
            return Response(results)
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)

class HumidityAverage(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            humidity = Retriever('7856d02822474b99b99155147202807').get_analyzer(city, date_start, date_end).humidity_average()
            data        = { 'humidity': {"average": humidity} }
            results     = SerializerHumidityAverage(data, many=False).data
            return Response(results)
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)

class HumidityMedian(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            humidity = Retriever('7856d02822474b99b99155147202807').get_analyzer(city, date_start, date_end).humidity_median()
            data     = { 'humidity': {"median": humidity} }
            results  = SerializerHumidityMedian(data, many=False).data
            return Response(results)
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)

class HumidityAll(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            analyzer = Retriever('7856d02822474b99b99155147202807').get_analyzer(city, date_start, date_end)
            data     = { 'humidity': {
                "minimum" : analyzer.humidity_min    (),
                "maximum" : analyzer.humidity_max    (),
                "average" : analyzer.humidity_average(),
                "median"  : analyzer.humidity_median ()} }
            results     = SerializerHumidityAll(data, many=False).data
            return Response(results)
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)

class TempAndHumidity(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            analyzer = Retriever('7856d02822474b99b99155147202807').get_analyzer(city, date_start, date_end)
            data     = {
                'temperature': {
                    "minimum" : analyzer.temperature_min    (),
                    "maximum" : analyzer.temperature_max    (),
                    "average" : analyzer.temperature_average(),
                    "median"  : analyzer.temperature_median ()},
                'humidity': {
                    "minimum" : analyzer.humidity_min    (),
                    "maximum" : analyzer.humidity_max    (),
                    "average" : analyzer.humidity_average(),
                    "median"  : analyzer.humidity_median ()} }
            results = SerializerTempAndHumidity(data, many=False).data
            return Response(results)
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)

class Graphs(views.APIView):
    def get(self, request, city=None, date_start=None, date_end=None):
        try:
            validate_request(city, date_start, date_end)
            data                 = {}
            data['city']         = city
            data['date_start']   = date_start
            data['date_end']     = date_end
            data['weather_data'] = Retriever('7856d02822474b99b99155147202807').get_raw_data(city, date_start, date_end)
            return render(request, 'graphs.html', context={ 'graph_data': json.dumps(data) })
        except Exception as e:
            error   = { 'error' : str(e) }
            results = SerializerError(error).data
            return Response(results)