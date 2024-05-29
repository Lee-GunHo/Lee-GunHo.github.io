print("20211127 이건호")

def sort_dict_total(x):
    return x["total"]
def cal_order(students):
    temp_students = sorted(students,key=sort_dict_total,reverse=True)
    order = 1

    for student in temp_students:
        student["order"]=order
        order=order+1
    return temp_students
def print_student(students):
    for student in students:
        print("이름:%s,총점:%s,등수:%s"%(student["name"],student["total"],student["order"]))
def main():
    students=[{"num":"1","name":"홍길동","total":"85","order":0},
              {"num":"2","name":"성춘향","total":"80","order":0},
              {"num":"3","name":"이몽룡","total":"90","order":0}]
    students=cal_order(students)
    print_student(students)

if __name__=="__main__":
    main()
    input()
    