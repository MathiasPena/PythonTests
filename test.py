#EXERCISE TEST

if __name__ == '__main__':
    
    records = list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        student = list((name, score))
        records.append(student)
        
    values = list(dict(records).values())
    values.sort()
    lowest = values[0]
    secondLowest = int()
    
    for v in values:
        if v == lowest:
            continue
        else:
            secondLowest = v
            break
            
    students = list()
    
    for e in records:
        for student in e:
            if type(student) is float and student == secondLowest:
                students.append(e)
                
    students.sort()
    
    for e in students:
        for student in e:
            if type(student) is str:
                print(student)
        