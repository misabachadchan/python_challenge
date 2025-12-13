class Student():
    def __init__(self):
        self.marks=[]

    def add_marks(self):
        for i in range(6):
            m=int(input("Enter marks:"))
            self.marks.append(m)

    def check_pass_fail(self):
        for m in self.marks:
            if m < 40:
                print("Result: FAIL")
                return
        print("Result: PASS")
       


    def Display(self):
        print("Marks",self.marks)


mark=Student()
mark.add_marks()
mark.Display()
mark.check_pass_fail()



