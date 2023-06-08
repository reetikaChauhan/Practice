class Person:
    def __init__(self,first_name,last_name,username,id_num):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = username
        self.id_num = id_num

    def __str__(self):
        return("First name : %s \nLast name : %s \nUsername : %s \nID : %s " % (self.first_name,self.last_name,self.user_name,self.id_num))

class Student(Person):
    def __init__(self, first_name, last_name, username, id_num):
        super().__init__(first_name, last_name, username, id_num)

class Instructor(Person):
    def __init__(self, first_name, last_name, username, id_num):
        super().__init__(first_name, last_name, username, id_num)

class TeachingAssistant(Person):
    def __init__(self, first_name, last_name, username, id_num):
        super().__init__(first_name, last_name, username, id_num)

class Parser():
    def __init__(self,students=[],instructors=[],tas=[]):
        self.students=students
        self.instructors =instructors
        self.tas = tas
    def parse(self,file_name):
        with open(file_name) as f:
            lines = f.readlines()
        for line in lines:
            l = line.strip().split(',')
            first_name = l[0]
            last_name = l[1]
            user_name = l[2]
            id_num = l[3]
            if l[4]== 'Student':
                s1 = Student(first_name,last_name,user_name,id_num)
                self.students.append(s1)
            elif l[4] == 'Instructor':
                i1 = Instructor(first_name,last_name,user_name,id_num)
                self.instructors.append(i1)
            elif l[4]=='TA':
                t1 = TeachingAssistant(first_name,last_name,user_name,id_num)
                self.tas.append(t1)

    def get_students(self):
        return self.students
    def get_instructors(self):
        return self.instructors
    def get_tas(self):
        return self.tas

class Main:
    def __init__(self):
        self.parse = Parser()
    def parse_file(self,filename):
        self.parse.parse(filename)
    def get_students(self,str1):
        student = []
        studentlist = self.parse.get_students()
        for j in studentlist:
            if str1 in j.id_num:
                student.append(j)
        return student

    def write_to_file(self,persons,filename):
        outfile = open(filename,'w')
        for k in persons:
            para = k.__str__()
            print('p',para)
            outfile.write(para+"\n"+"\n")
        outfile.close()






        

