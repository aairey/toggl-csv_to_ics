# toggl-csv_to_ics

This Python script provides a way to convert an export of [Toggl](http://www.toggl.com/) time entries in CSV format to ICS.
Allowing you to import it into any calendar application.

Some specific changes were made, e.g. concatenating fields so that the event name becomes:

`Client - Project: Description - User`

The Email, Task and Billable fields are ignored as I personally do not want them in my calendar app.
The Location of the calendar events is set to the username of the Toggl user.

## Requirements

You need the followin to be able to run this code:

* Python >= 2.7
* icalendar >= 3.4 (`pip install icalendar`)

## Usage

First install the script and it's requirements:

```
git clone https://github.com/aairey/toggl-csv_to_ics
cd toggl-csv_to_ics
pip install requirements.txt
```

Export a detailed CSV from [Toggl](https://support.toggl.com/detailed-reports-toggl-new/#export) and save it in the same folder as `toggl.csv`.

Then run the script as follows:
```
python toggl-csv_to_ics.py
```

A file called `toggl.ics` will be generated, which you can import into your calendar application.


## Contributing

Feel free to create your own issues or pull requests.

## Credits

The code from convert.py was borrowed from [csv-to-ical](https://github.com/albertyw/csv-to-ical).
