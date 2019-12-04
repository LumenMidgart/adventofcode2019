file_name = input('Enter file name:')
file_handle = open(file_name)
total_mass = 0;
total_fuel = 0
masa_individual = 0
for line in file_handle:
    total_mass += int(line)
    masa_individual = int(line)
    total_fuel += int(masa_individual/3)-2    
# print(total_mass)
print(total_fuel) 