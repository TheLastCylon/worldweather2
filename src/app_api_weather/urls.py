from django.urls import include, path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('<str:city>/<str:date_start>/<str:date_end>'                    , views.TempAndHumidity.as_view()),
    path('<str:city>/<str:date_start>/<str:date_end>/temperature/min'    , views.TemperatureMinimum.as_view()),
    path('<str:city>/<str:date_start>/<str:date_end>/temperature/max'    , views.TemperatureMaximum.as_view()),
    path('<str:city>/<str:date_start>/<str:date_end>/temperature/average', views.TemperatureAverage.as_view()),
    path('<str:city>/<str:date_start>/<str:date_end>/temperature/median' , views.TemperatureMedian.as_view()),
    path('<str:city>/<str:date_start>/<str:date_end>/temperature'        , views.TemperatureAll.as_view()),
    path('<str:city>/<str:date_start>/<str:date_end>/humidity/min'       , views.HumidityMinimum.as_view()),
    path('<str:city>/<str:date_start>/<str:date_end>/humidity/max'       , views.HumidityMaximum.as_view()),
    path('<str:city>/<str:date_start>/<str:date_end>/humidity/average'   , views.HumidityAverage.as_view()),
    path('<str:city>/<str:date_start>/<str:date_end>/humidity/median'    , views.HumidityMedian.as_view()),
    path('<str:city>/<str:date_start>/<str:date_end>/humidity'           , views.HumidityAll.as_view()),
    path('<str:city>/<str:date_start>/<str:date_end>/graphs'             , views.Graphs.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]