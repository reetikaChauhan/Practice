import os
def load_car_list(car_data):
    with open(car_data) as f:
        lines = f.readlines()
        return list(tuple(line.rstrip('\n').split(',')) for line in lines)
cars_list=load_car_list('car_data')

def load_car_dict(car_data):
    with open(car_data) as f:
        lines = f.readlines()
        cars_listt = list(tuple(line.rstrip('\n').split(',')) for line in lines)
    car_dict = {i[4]: i for i in cars_listt}   #creating dictionary with key as id and values as car which is a tuple
    return car_dict
#car_dict = load_car_dict(cars_list)

def cars_with_make(cars_list,make):
    car_make = []                      # creating a function to create list of cars of given make
    for i in cars_list:
        if i[1] == make:
            car_make.append(i)
    return car_make

#print(cars_with_make(cars_list,'Cadillac'))

def cars_with_color(cars_list,color):     # creating a function to create list of cars of given color
    car_color=[]
    for i in cars_list:
        if i[2] == color:
            car_color.append(i)
    return car_color

#print(cars_with_color(cars_list,'Green'))

def sort_by_year(car_list):           # created a new dictionary which is sorted by year
    car_listsort = car_list
    for i in range(len(car_listsort)):
        min_index = i
        for j in range(i+1, len(car_listsort)):
            if (int(car_listsort[min_index][3] )> int(car_listsort[j][3])):
                min_index = j
        car_listsort[i], car_listsort[min_index] = car_listsort[min_index], car_listsort[i]
    return car_listsort

#print(sort_by_year(cars_list))

def remove_car(car_dict,key):        # remove car of particular id otherwise raise error
    try:
        del car_dict[key]
    except KeyError:
        print('key is not found')
    

#remove_car(car_dict,"49")

def print_make_count(car_list):         # count of cars of each make
    l=[]
    d={}
    for car in car_list:
        if not car[0] in l:
            l.append(car[0])
            d[car[0]] = 1
        else:
            d[car[0]] += 1
    
    for make in d:
        print(make + ' ' + str(d[make]))

def write_to_file(car_dict,file_name):      # writing dictionary to a new file (file_name)
    desktop = os.path.join(os.path.expanduser("~"), "Desktop") # creating path for files to write
    filePath = os.path.join(desktop, file_name)
    outfile = open(filePath,'w')
    line=''
    for v in car_dict.values():
        for t in v:
            line += str(t)+ ',' 
        outfile.write(line+"\n")
        line=""
        
    outfile.close()
    

#write_to_file(car_dict,'file_name')

