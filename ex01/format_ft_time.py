import time

current_time = time.time()

current_time_format = "{:,.10f}".format(current_time)
scientific_notation = "{:.2e}".format(current_time)

print("Seconds since January 1, 1970:", current_time_format, "or", scientific_notation, "in scientific notation")

local_time = time.localtime(current_time)
formatted_date = time.strftime("%B %d %Y", local_time)

print(formatted_date)
