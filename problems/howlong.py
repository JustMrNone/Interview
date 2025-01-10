def format_duration(seconds: int) -> str:
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365
    
    if seconds < 0:
        return "invalid number"
    
    if seconds == 0:
        return "now"
    
    if seconds < minute:
        return f"{seconds} seconds"
    
    if seconds < hour:
        minutes = seconds // minute
        remaining_seconds = seconds % minute
        return f"{minutes} minutes, {remaining_seconds} seconds"
    
    if seconds < day:
        hours = seconds // hour
        remaining_minutes = (seconds % hour) // minute
        remaining_seconds = seconds % minute
        return f"{hours} hours, {remaining_minutes} minutes, {remaining_seconds} seconds"
    
    if seconds < year:
        days = seconds // day
        remaining_hours = (seconds % day) // hour
        remaining_minutes = (seconds % hour) // minute
        remaining_seconds = seconds % minute
        return f"{days} days, {remaining_hours} hours, {remaining_minutes} minutes, {remaining_seconds} seconds"
    if seconds > year:
        years = seconds // year
        remaining_days = (seconds % year) // day
        remaining_hours = (seconds % day) // hour
        remaining_minutes = (seconds % hour) // minute
        remaining_seconds = seconds % minute
        return f"{years} years, {remaining_days} days, {remaining_hours} hours, {remaining_minutes} minutes, {remaining_seconds} seconds"

numb = int(input())       
print(format_duration(numb))
