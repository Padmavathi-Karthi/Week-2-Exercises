# Consider the following scenario about using if-elif-else statements:
# Police patrol a specific stretch of dangerous highway and are very particular about speed limits.  The speed limit is 65 miles per hour. Cars going 80 miles per hour or more are given a “Reckless Driving” ticket. Cars going more than 65 miles per hour are given a “Speeding” ticket.  Any cars going less than that are labeled “Safe” in the system.

def speeding_ticket(speed):
    if speed > 80:
        ticket = "Reckless Driving"
    elif speed > 65:
        ticket = "Speeding"
    else:
        ticket = "Safe"
    return ticket


print(speeding_ticket(87)) # Should print Reckless Driving
print(speeding_ticket(66)) # Should print Speeding
print(speeding_ticket(65)) # Should print Safe
print(speeding_ticket(85)) # Should print Reckless Driving
print(speeding_ticket(35)) # Should print Safe
print(speeding_ticket(77)) # Should print Speeding