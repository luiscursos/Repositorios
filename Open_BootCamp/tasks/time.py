from time import strptime, localtime, time

knock_off = strptime("1900"[:2],"%H")[3]
current_time = localtime()[3]
result = current_time-knock_off

if current_time>=knock_off :
    print("It`s time go to home ")
elif 8 < current_time <= 19:
    print("It's time of work") 
else:
    print(result,"hours left to get off works")





# current_hour=(localtime()[3])
# #current_minut=(localtime()[4])

# knock_off_hour = strptime("07:00"[:2],"%H")[3]
# #knock_off_minut = strptime("07:00"[3:5],"%M")[4]



