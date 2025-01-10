def format_duration(seconds):
    if seconds < 0:
        return "invalid number"
    
    if seconds == 0:
        return "now"

    # Define time units in seconds
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365

    # Compute each unit
    years = seconds // year
    seconds %= year
    days = seconds // day
    seconds %= day
    hours = seconds // hour
    seconds %= hour
    minutes = seconds // minute
    seconds %= minute

    # Build the result
    parts = []
    if years > 0:
        parts.append(f"{years} year" + ("s" if years > 1 else ""))
    if days > 0:
        parts.append(f"{days} day" + ("s" if days > 1 else ""))
    if hours > 0:
        parts.append(f"{hours} hour" + ("s" if hours > 1 else ""))
    if minutes > 0:
        parts.append(f"{minutes} minute" + ("s" if minutes > 1 else ""))
    if seconds > 0:
        parts.append(f"{seconds} second" + ("s" if seconds > 1 else ""))

    # Join the parts with proper grammar
    if len(parts) > 1:
        return ", ".join(parts[:-1]) + " and " + parts[-1]
    else:
        return parts[0]