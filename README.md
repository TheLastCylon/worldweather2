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


<!-- ========================================================================================================================= -->
### Minimum
| | |
| --- | --- |
| Request</td><td><code>/wwapi/<b>[CITY-NAME]</b>/<b>[START-DATE]</b>/<b>[END-DATE]</b>/temperature/min</code></td></tr>
| Returns</td><td><code>minimum temperature, for specified period</code></td></tr>
| Example</td><td><code>http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/temperature/min</code></td></tr>
| Result </td><td><code>{ "temperature": { "minimum": 16.0 } }</code></td></tr>
</table>
</li>

<!-- ========================================================================================================================= -->
<li><h4>Maximum</h4>
<table>
   <tr class="row1"><td class="head">Request</td><td><code>/wwapi/<b>[CITY-NAME]</b>/<b>[START-DATE]</b>/<b>[END-DATE]</b>/temperature/max</code></td></tr>
   <tr class="row2"><td class="head">Returns</td><td><code>maximum temperature, for specified period</code></td></tr>
   <tr class="row1"><td class="head">Example</td><td><code>http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/temperature/max</code></td></tr>
   <tr class="row2"><td class="head">Result </td><td><code>{ "temperature": { "maximum": 29.0 } }</code></td></tr>
</table>
</li>

<!-- ========================================================================================================================= -->
<li><h4>Average</h4>
<table>
   <tr class="row1"><td class="head">Request</td><td><code>/wwapi/<b>[CITY-NAME]</b>/<b>[START-DATE]</b>/<b>[END-DATE]</b>/temperature/average</code></td></tr>
   <tr class="row2"><td class="head">Returns</td><td><code>average temperature, for specified period</code></td></tr>
   <tr class="row1"><td class="head">Example</td><td><code>http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/temperature/average</code></td></tr>
   <tr class="row2"><td class="head">Result </td><td><code>{ "temperature": { "average": 21.419354838709676 } }</code></td></tr>
</table>
</li>

<!-- ========================================================================================================================= -->
<li><h4>Median</h4>
<table>
   <tr class="row1"><td class="head">Request</td><td><code>/wwapi/<b>[CITY-NAME]</b>/<b>[START-DATE]</b>/<b>[END-DATE]</b>/temperature/median</code></td></tr>
   <tr class="row2"><td class="head">Returns</td><td><code>median temperature, for specified period</code></td></tr>
   <tr class="row1"><td class="head">Example</td><td><code>http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/temperature/median</code></td></tr>
   <tr class="row2"><td class="head">Result </td><td><code>{ "temperature": { "median": 21.0 } }</code></td></tr>
</table>
</li>
</ul>
<!-- ========================================================================================================================= -->

<h3>Humidity</h3>
<ul>
<li><h4>All Humidity data</h4>
<table>
   <tr class="row1"><td class="head">Request</td><td><code>/wwapi/<b>[CITY-NAME]</b>/<b>[START-DATE]</b>/<b>[END-DATE]</b>/humidity</code></td></tr>
   <tr class="row2"><td class="head">Returns</td><td><code>all humidity data, for specified period</code></td></tr>
   <tr class="row1"><td class="head">Example</td><td><code>http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/humidity</code></td></tr>
   <tr class="row2"><td class="head">Result </td><td><code>{ "humidity": { "minimum": 36.0, "maximum": 90.0, "average": 68.58467741935483, "median": 70.0 } }</code></td></tr>
</table>
</li>

<!-- ========================================================================================================================= -->
<li><h4>Minimum</h4>
<table>
   <tr class="row1"><td class="head">Request</td><td><code>/wwapi/<b>[CITY-NAME]</b>/<b>[START-DATE]</b>/<b>[END-DATE]</b>/humidity/min</code></td></tr>
   <tr class="row2"><td class="head">Returns</td><td><code>minimum humidity, for specified period</code></td></tr>
   <tr class="row1"><td class="head">Example</td><td><code>http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/humidity/min</code></td></tr>
   <tr class="row2"><td class="head">Result </td><td><code>{ "humidity": { "minimum": 36.0 } }</code></td></tr>
</table>
</li>

<!-- ========================================================================================================================= -->
<li><h4>Maximum</h4>
<table>
   <tr class="row1"><td class="head">Request</td><td><code>/wwapi/<b>[CITY-NAME]</b>/<b>[START-DATE]</b>/<b>[END-DATE]</b>/humidity/max</code></td></tr>
   <tr class="row2"><td class="head">Returns</td><td><code>maximum humidity, for specified period</code></td></tr>
   <tr class="row1"><td class="head">Example</td><td><code>http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/humidity/max</code></td></tr>
   <tr class="row2"><td class="head">Result </td><td><code>{ "humidity": { "maximum": 90.0 } }</code></td></tr>
</table>
</li>

<!-- ========================================================================================================================= -->
<li><h4>Average</h4>
<table>
   <tr class="row1"><td class="head">Request</td><td><code>/wwapi/<b>[CITY-NAME]</b>/<b>[START-DATE]</b>/<b>[END-DATE]</b>/humidity/average</code></td></tr>
   <tr class="row2"><td class="head">Returns</td><td><code>average humidity, for specified period</code></td></tr>
   <tr class="row1"><td class="head">Example</td><td><code>http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/humidity/average</code></td></tr>
   <tr class="row2"><td class="head">Result </td><td><code>{ "humidity": { "average": 68.58467741935483 } }</code></td></tr>
</table>
</li>

<!-- ========================================================================================================================= -->
<li><h4>Median</h4>
<table>
   <tr class="row1"><td class="head">Request</td><td><code>/wwapi/<b>[CITY-NAME]</b>/<b>[START-DATE]</b>/<b>[END-DATE]</b>/humidity/median</code></td></tr>
   <tr class="row2"><td class="head">Returns</td><td><code>median humidity, for specified period</code></td></tr>
   <tr class="row1"><td class="head">Example</td><td><code>http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/humidity/median</code></td></tr>
   <tr class="row2"><td class="head">Result </td><td><code>{ "humidity": { "median": 70.0 } }</code></td></tr>
</table>
</li>
</ul>

<!-- ========================================================================================================================= -->
<h3>Feeling Greedy?</h3>
<ul>
<li><h4>Get everything</h4>
<table>
   <tr class="row1"><td class="head">Request</td><td><code>/wwapi/<b>[CITY-NAME]</b>/<b>[START-DATE]</b>/<b>[END-DATE]</b></code></td></tr>
   <tr class="row2"><td class="head">Returns</td><td><code>all temperature and humidity data, for the specified period</code></td></tr>
   <tr class="row1"><td class="head">Example</td><td><code>http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31</code></td></tr>
   <tr class="row2"><td class="head">Result </td><td><code>{ "temperature": { "minimum": 16.0, "maximum": 29.0, "average": 21.419354838709676, "median": 21.0 }, "humidity": { "minimum": 36.0, "maximum": 90.0, "average": 68.58467741935483, "median": 70.0 } }</code></td></tr>
</table>
</li>
</ul>

<h3>Dealing with errors</h3>
<p>All API errors will be reported as in the example below.</p>
<table>
   <tr class="row1"><td class="head">Result</td><td><code>{"error": "Date values must be provided in YYYY-MM-DD format!"}</code></td></tr>
</table>

<h3>Graphs</h3>
<p>You can see some rather nice maximum/minimum graphs for the period you specified by using</p>
<table>
   <tr class="row1"><td class="head">Request</td><td><code>/wwapi/<b>[CITY-NAME]</b>/<b>[START-DATE]</b>/<b>[END-DATE]</b>/graphs</b></code></td></tr>
   <tr class="row2"><td class="head">Returns</td><td><code>See the data in neat graphs :)</code></td></tr>
   <tr class="row1"><td class="head">Example</td><td><code>http://localhost:8000/wwapi/Cape%20Town/2020-01-01/2020-01-31/graphs</code></td></tr>
</table>
