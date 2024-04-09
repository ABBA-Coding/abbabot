from django.test import TestCase

from datetime import datetime


def days_since_event(event_date):
    """
    Calculate the number of days since the event date.

    Parameters:
        event_date (str): The date of the event in the format 'YYYY-MM-DD'.

    Returns:
        int: Number of days since the event.
    """
    event_date = datetime.strptime(event_date, '%Y-%m-%d').date()
    current_date = datetime.now().date()
    delta = current_date - event_date
    return delta.days


# Example usage:
event_date = '2024-04-08'  # Change this to the date of the event
days_since = days_since_event(event_date)
print("Days since the event:", days_since)