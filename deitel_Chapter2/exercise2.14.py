print("Heart rate calculator")

users_age = int(input("Enter your age: "))
rate = 220
heart_rate_beat_per_minute = rate - users_age
percent = 100

percent_rate1 = 50/percent
percent_rate2 = 85/percent

max_beat1 = percent_rate1 * users_age
max_beat2 = percent_rate2 * users_age


print("Your maximum heart beat rate is between the range of", max_beat1, "to", max_beat2)
