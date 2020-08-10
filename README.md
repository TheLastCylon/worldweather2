# worldweather
## Welcome to the World Weather App.
This is a quick and dirty demonstration of using Django to provide a rest-full API.
The application grabs weather data from a provider site, which is then manipulated and formed for our purposes.
Although we have access to incredibly detailed data via our provider, we only use the humidity and temperature data-points for this demonstration.

### A few things to note about the API this app provides:
- All testing was done with Python 3.5
- All interfaces are accessed via GET operation.</li>
- All interfaces require three parameters:

| Field          | Description                   |
| -------------- | ----------------------------- |
| **city**       | A valid city name             |
| **start date** | A date in the form YYYY-MM-DD |
| **end date**   | A date in the form YYYY-MM-DD |

These parameters are provided to the API via dynamic URL in the form: ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]```

Note that **end-date** must be a date that falls after **start-date** and that the two dates may not be more than **31** days apart.
This limitation is on the part of the data provider.

## The API
The provided API can be broken into two groups: Temperature and Humidity.
### Temperature
#### All Temperature data
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]/temperature``` |
| Returns | ```all temperature data, for specified period``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/temperature``` |
| Result  | ```{ "temperature": { "minimum": 16.0, "maximum": 29.0, "average": 21.419354838709676, "median": 21.0 } }``` |

#### Minimum
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]/temperature/min``` |
| Returns | ```minimum temperature, for specified period``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/temperature/min``` |
| Result  | ```{ "temperature": { "minimum": 16.0 } }``` |

#### Maximum
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]/temperature/max``` |
| Returns | ```maximum temperature, for specified period``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/temperature/max``` |
| Result  | ```{ "temperature": { "maximum": 29.0 } }``` |

#### Average
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]/temperature/average``` |
| Returns | ```average temperature, for specified period``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/temperature/average``` |
| Result  | ```{ "temperature": { "average": 21.419354838709676 } }``` |

#### Median
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]/temperature/median``` |
| Returns | ```median temperature, for specified period``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/temperature/median``` |
| Result  | ```{ "temperature": { "median": 21.0 } }``` |

### Humidity
#### All Humidity data
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]/humidity``` |
| Returns | ```all humidity data, for specified period``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/humidity``` |
| Result  | ```{ "humidity": { "minimum": 36.0, "maximum": 90.0, "average": 68.58467741935483, "median": 70.0 } }``` |

#### Minimum
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]/humidity/min``` |
| Returns | ```minimum humidity, for specified period``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/humidity/min``` |
| Result  | ```{ "humidity": { "minimum": 36.0 } ``` |

#### Maximum
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]/humidity/max``` |
| Returns | ```maximum humidity, for specified period``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/humidity/max``` |
| Result  | ```{ "humidity": { "maximum": 90.0 } ``` |

#### Average
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]/humidity/average``` |
| Returns | ```average humidity, for specified period``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/humidity/average``` |
| Result  | ```{ "humidity": { "average": 68.58467741935483 } ``` |

#### Median
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]/humidity/median``` |
| Returns | ```median humidity, for specified period``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/humidity/median``` |
| Result  | ```{ "humidity": { "median": 70.0 } ``` |

### Feeling Greedy?
#### Get everything
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE``` |
| Returns | ```all temperature and humidity data, for the specified period``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31``` |
| Result  | ```{ "temperature": { "minimum": 16.0, "maximum": 29.0, "average": 21.419354838709676, "median": 21.0 }, "humidity": { "minimum": 36.0, "maximum": 90.0, "average": 68.58467741935483, "median": 70.0 } ``` |

### Dealing with errors
All API errors will be reported as in the example below.
| | |
| --- | --- |
| Result | ```{"error": "Date values must be provided in YYYY-MM-DD format``` |

### Graphs
You can see some rather nice maximum/minimum graphs for the period you specified by using
| | |
| --- | --- |
| Request | ```/wwapi/[CITY-NAME]/[START-DATE]/[END-DATE]/graphs``` |
| Returns | ```See the data in neat graphs ``` |
| Example | ```http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/graphs``` |

