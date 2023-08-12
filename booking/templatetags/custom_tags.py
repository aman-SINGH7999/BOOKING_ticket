from django import template
register = template.Library()

@register.filter(name='times')
def times(number):
    return range(number)

@register.filter(name='is_booked')
def is_booked(seat_no,array):
    if seat_no in array:
        return True
    return False