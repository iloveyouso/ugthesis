# OPTION 1 #

import sys
import var_infer_bj
from log_generator import generate_apdl_script
import math

def map_circle_data(circle_data):
    num_circles = circle_data[0]
    circles = circle_data[1:]
    
    mapped_circles = []
    scale_factor = math.sqrt(3000 * 1000 / (512 * 512))
    
    for circle in circles:
        x1, x2, radius = circle
        new_x1 = 1500 / 256 * (x2 - 256)
        new_x2 = 500 / 256 * (-x1 + 256)
        new_radius = radius * scale_factor
        mapped_circles.append([new_x1, new_x2, new_radius])
    
    mapped_circle_data = [num_circles] + mapped_circles
    return mapped_circle_data

# Original circle data
circle_data = [5, [50, 50, 30], [100, 100, 40], [150, 150, 50], [200, 200, 60], [250, 250, 70]]

# Map the circle data
mapped_circle_data = map_circle_data(circle_data)

print(mapped_circle_data)

if len(sys.argv) < 2:
    print("Please provide the .png file name as an argument.")
    sys.exit(1)

png_file = sys.argv[2]
print(f"Processing {png_file}...")

path = png_file.replace("images/", "").replace(".png", "")

# # Assuming circle_data is defined somewhere
# circle_data = [5, [50, 50, 30], [100, 100, 40], [150, 150, 50], [200, 200, 60], [250, 250, 70]]

# Generate APDL script using the combined data
circle_data = var_infer_bj.start()
print('returned from var_infer.py is: ', str(circle_data))

mapped_circle_data = map_circle_data(circle_data)
print('mapped_circle_data is: ', str(mapped_circle_data))

generate_apdl_script(mapped_circle_data,path)

# ########### OPTION 2 #########

# import sys
# import subprocess
# from log_generator import generate_apdl_script

# if len(sys.argv) < 2:
#     print("Please provide the .png file name as an argument.")
#     sys.exit(1)


# png_file = sys.argv[1]
# print(f"Processing {png_file}...")

# # Call var_infer.py with the necessary arguments
# try:
#     result = subprocess.run(
#         ['python', 'var_infer.py', '--image', png_file],
#         check=True,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         text=True
#     )
#     print(result.stdout)
# except subprocess.CalledProcessError as e:
#     print(f"Error occurred: {e.stderr}")
    


# # Assuming circle_data is defined somewhere
# circle_data = [5, [50, 50, 30], [100, 100, 40], [150, 150, 50], [200, 200, 60], [250, 250, 70]]
# generate_apdl_script(circle_data)

# # Receive the list returned by var_infer.py
# output_list = result.stdout.splitlines()