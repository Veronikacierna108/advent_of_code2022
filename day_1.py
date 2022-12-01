with open('input1.txt', encoding='utf-8') as input_data:
    rows = input_data.readlines()
  
# 65401, 65413, 66487
def find_max_calories(input_data):
    list_of_elfs =  []
    x = 0
    for i in input_data:
        if i != '\n':
            x += int(i) 
        else:
            list_of_elfs.append(x)
            x = 0 
    list_of_elfs.sort()


        
    print(max(list_of_elfs)) #elf carrying the most calories
    print(sum(list_of_elfs[-3:])) #top three elf carrieng the most calories
        

        
find_max_calories(rows)

