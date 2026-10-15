try:
    distance = float(input("Distance (meters): "))
    time = input("Total time (minutes:seconds): ")

    minutes_text, seconds_text = time.split(":")
    minutes = int(minutes_text)
    seconds = int(seconds_text)

except ValueError:
    print("Enter a numeric distance and a time like 8:20.")

else:
    total_seconds = minutes * 60 + seconds

    if distance <= 0:
        print("Distance must be greater than zero.")
    elif minutes < 0 or seconds < 0 or seconds >= 60:
        print("Minutes must be nonnegative and seconds must be 0–59.")
    elif total_seconds == 0:
        print("Total time must be greater than zero.")
    else:
        split_seconds = round(total_seconds * 500 / distance)

        split_minutes = split_seconds // 60
        split_remainder = split_seconds % 60

        print(
            "Average split: %d:%02d /500m"
            % (split_minutes, split_remainder)
        )