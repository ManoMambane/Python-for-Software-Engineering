swimming_time = float(input("Enter swimming time (minutes): "))
cycling_time = float(input("Enter cycling time (minutes): "))
running_time = float(input("Enter running time (minutes): "))

total_time = swimming_time + cycling_time + running_time

print(f"Total time taken for the triathlon: {total_time} minutes")

if total_time <= 100:
    award = "Provincial colours"
elif total_time <= 105:
    award = "Provincial half colours"
elif total_time <= 110:
    award = "Provincial scroll"
else:
    award = "No award"

print(f"Award: {award}")