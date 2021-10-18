## Opening Hours

An app that takes JSON-formatted opening hours of a restaurant
as an input and outputs hours in more human readable format.

### TechStack:
- Python 3.8

#### How to run:
Install requirements:
> pip install -r requirements.txt


Run server:
> python manage.py runserver

API URL (POST):
> http://127.0.0.1:8000/api/opening-hours/

##### Sample Input:
```
{
    "friday": [
      {
        "type": "open",
        "value": 64800
      }
    ],
    "saturday": [
      {
        "type": "close",
        "value": 3600
      },
      {
        "type": "open",
        "value": 32400
      },
      {
        "type": "close",
        "value": 39600
      },
      {
        "type": "open",
        "value": 57600
      },
      {
        "type": "close",
        "value": 82800
      }
    ]
  }
```

##### Sample Output:
``` 
{
   "Friday": "6 PM - 1 AM",
   "Saturday": "9 AM - 11 AM, 4 PM - 11 PM"
}
```


#### Tests:
> python manage.py test


### Ideas to improve the data structure:
As the context about the current data format is limited for me, I could only come up with the 
following ideas:

- Instead of putting over-night closing time to next day, we can put it in the same day dict.
 This will simplify the conversion.
- We can also store the time as a list of tuple [(open_hour, close_hour), (open_hour, close_hour)] against a day key.
 
 