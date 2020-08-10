import datetime

#--------------------------------------------------------------------------------
def validate_request(city, date_start, date_end):
    max_date_delta = datetime.timedelta(days=31) # We provide for a maximum of 31 days worth of data for now.

    if not city or not isinstance(city, str) or len(city) <= 0:
        raise ValueError("Invalid city parameter provided!")
    
    try:
        start_date = datetime.datetime.strptime(date_start, '%Y-%m-%d')
        end_date   = datetime.datetime.strptime(date_end, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Date values must be provided in YYYY-MM-DD format!")

    if (end_date - start_date) > max_date_delta:
        raise ValueError("Provided dates may not be more than 31 days appart!")
