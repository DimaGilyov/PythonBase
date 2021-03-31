time_in_seconds = int(input("Enter time in seconds: "))

hours = (time_in_seconds // 3600) % 24
minutes = (time_in_seconds // 60) % 60
seconds = time_in_seconds % 60

print(f"Time {hours:02d}:{minutes:02d}:{seconds:02d}")
