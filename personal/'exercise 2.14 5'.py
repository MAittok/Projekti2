'teht 6.9'
import math

def day_name(x):
    if x > 6:
       return None
    
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    months = ["January", 'February', 'March', 'May', 'April', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print (days[x])
    return days[x]
    
    
def day_num(y):
    if y == 'Sunday':
        return 0
    if y == 'Monday':
        return 1
    if y == 'Tuesday':
        return 2
    if y == 'Wednesday':
        return 3
    if y == 'Thursday':
        return 4
    if y == 'Friday':
        return 5
    if y == 'Saturday':
        return 6
    else:
        return None

def day_counter(day, z):
    u = day_num(day)
    print(z)
    for i in range(z):
        u = u + 1        
        
        if u > 6:
           u = 0
    day_name(u)


def days_in_month(month):

    if month in ['September', 'April', 'June', 'November']:
        return 30

    if month in ['January', 'March', 'May', 'July', 'August','October','December']:
        return 31        

    if month == 'February':
        return 28

    else:
        return None


def to_secs(h,min,sec):
    htomin = h*60
    mintosec = (htomin + min) * 60
    total = mintosec + sec
    print (int(total))


def hours_in(sec):
    min = sec/60
    hour = min/60
    print(int(hour))

def minutes_in(sec):
    min = sec/60
    hour = min/60
    koko = (int(hour))
    jaannos = hour-koko
    tulos = 60 * jaannos
    print(int(tulos))   

def seconds_in(sec):
    min = sec/60
    hour = int(min)/60
    print(hour)
    minuutit = min - (int(hour)*60)
    print(minuutit)
    sekuntit = (minuutit - (int(minuutit))) * 60
    print(int(sekuntit))
    

def compare(a,b):
    if (a == b):
        return 0
    if (a > b):
        return 1
    else:
        return -1

def hypotenuse(leg1, leg2):
    tulo = leg1**2 + leg2**2
    hypo = math.sqrt(tulo)

    return hypo