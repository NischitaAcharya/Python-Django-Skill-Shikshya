recharge_pin = "2345 2344 5657 6767"
splited_recharge_pin = recharge_pin.split(" ")
# print(splited_recharge_pin)

encoded_list =[]
for i in range (len(splited_recharge_pin)-1):
    encoded_string = "****"
    encoded_list.append(encoded_string)
    # print(splited_recharge_pin[i])
    
encoded_list.append(splited_recharge_pin[-1])

output =" ".join(encoded_list)
print(output)
# print(encoded_list)


# Loop through all parts except the last one
# Replace each character with '*'
# Add the last part as it is
# Join the list back into a string
# Print the final result
 
recharge_pin = "234567 75644 3452 297 345"
splited_recharge_pin = recharge_pin.split(" ")

encoded_list = []

for i in range(len(splited_recharge_pin) - 1):
    encoded_string = "*" * len(splited_recharge_pin[i])
    encoded_list.append(encoded_string)

encoded_list.append(splited_recharge_pin[-1])

output = " ".join(encoded_list)
print(output)
