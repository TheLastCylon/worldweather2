import json
import requests
from .analyzer import Analyzer

class Retriever:

  #--------------------------------------------------------------------------------
  def __init__(self, api_key):
    self.city          = ''
    self.date_start    = ''
    self.date_end      = ''
    self.api_key       = api_key
    self.data_analyzer = Analyzer()

  #--------------------------------------------------------------------------------
  def request_changed(self, city, date_start, date_end):
    return ((city != self.city ) or (date_start != self.date_start) or (date_end != self.date_end))
  
  #--------------------------------------------------------------------------------
  def get_raw_data(self, city, date_start, date_end):
    try:
      url      = self.format_url(city, date_start, date_end)
      html_raw = requests.get(url)
      data     = html_raw.json()

      if 'error' in data['data'].keys():
        error_message = data['data']['error'][0]['msg']
        raise Exception("World Weather Online reports:" + error_message)

      retval = {}

      for day_data in data['data']['weather']:
        humidity_data = []
        for hour_data_point in day_data['hourly']:
          humidity_data.append(hour_data_point['humidity'])

        retval[day_data['date']] = {
          'temperature': {
            'min': float(day_data['mintempC']),
            'max': float(day_data['maxtempC'])
            },
          'humidity': {
            'min': float(min(humidity_data)),
            'max': float(max(humidity_data))
            }
          }

      return retval

    except Exception as e:
      raise Exception('World Weather Data retriever: Could not retrieve data: ' + str(e))

  #--------------------------------------------------------------------------------
  def get_analyzer(self, city, date_start, date_end):
    if not self.request_changed(city, date_start, date_end) and self.data_analyzer: # If there was no change, we don't need to hit the worldweatheronline api again.
      return self.data_analyzer

    try:
      url      = self.format_url(city, date_start, date_end)
      html_raw = requests.get(url)
      data     = html_raw.json()

      if 'error' in data['data'].keys():
        error_message = data['data']['error'][0]['msg']
        raise Exception("World Weather Online reports:" + error_message)

      self.data_analyzer.set_data(html_raw.json())

      self.city       = city
      self.date_start = date_start
      self.date_end   = date_end

      return self.data_analyzer
    except Exception as e:
      raise Exception('World Weather Data retriever: Could not retrieve data: ' + str(e))

  def format_url(self, city, date_start, date_end):
      return ("http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key={}&q={}&format=json&date={}&enddate={}".format(self.api_key, city, date_start, date_end))

#--------------------------------------------------------------------------------
if __name__ == "__main__":
  raise Exception('World Weather Data retriever: Not meant for direct execution.')
