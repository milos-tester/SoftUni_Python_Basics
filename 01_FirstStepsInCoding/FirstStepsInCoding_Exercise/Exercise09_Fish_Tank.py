length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage = float(input())
volume_of_aquarium = length_cm * width_cm * height_cm
volume_in_liters = volume_of_aquarium / 1000
occupied_space = percentage / 100
required_liters = volume_in_liters * (1-occupied_space)
print(required_liters)