
def getFuel(masa):
    m = int(masa)
    #print("get número llamado con masa: ", m)
    if m <= 0:
        return 0
    else:        
        fuel = int(m/3)-2
        res = 0
        if fuel > 0:
            #print("fuel: ", fuel)
            res = fuel + getFuel(fuel)        
        return res

file_name = input('Enter file name:')
file_handle = open(file_name)
total_mass = 0
total_fuel = 0
masa_individual = 0
for line in file_handle:
    masa_individual = int(line)
    total_fuel += getFuel(masa_individual)

print(total_fuel)  # 4903759
