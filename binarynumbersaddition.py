class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry='0'
        sum =''
        a = list(a)
        b = list(b)
        if len(a)>len(b):
            for i in range(len(b),len(a)):
                b.insert(0,'0')
        else:
            for i in range(len(a),len(b)):
                a.insert(0,'0')    
        a=list(reversed(a))
        b=list(reversed(b))
        print(a)
        print(b)
        for (i,j) in zip(a,b):
            print("i",i,"j",j)
            if (i=='1') and (j=='1'):
                if carry == '0':
                    print("hi")
                    sum = '0'+ sum
                    carry='1'
                elif carry=='1':
                    sum = '1'+ sum
                    carry='1'
            if i=='1' and j=='0':
                if carry=='0':
                    sum = '1'+ sum
                    carry='0'
                elif carry=='1':
                    sum = '0'+ sum
                    carry='1'
            if i=='0' and j=='1':
                if carry =='0':
                    sum = '1'+ sum
                    carry='0'
                elif carry=='1':
                    sum = '0'+ sum
                    carry='1'
            if i=='0' and j=='0':
                if carry =='0':
                    sum = '0'+ sum
                    carry='0'
                elif carry=='1':
                    sum = '1'+ sum
                    carry='0'
            print(sum)
        if carry=='1':
            sum = '1'+ sum
        return str(sum)
        #return bin(int(a,2) + int(b,2))[2:]
        #convert a and b strings into binary values of base 2
        #result = int(a, 2) + int(b, 2)
        #convert result from integer to binary format
        #return format(result, "b")



        

        