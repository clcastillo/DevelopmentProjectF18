#Project_3_Shirley_Lin
#
class Group_1(GroupMember):

    def __init__(self,day,time):
        self.day=day
        self.time=time
            
    def meet_up(self):
        for i in range(1,4):
            while(name[i]):
                if (classSchedule[i]!=classSchedule[i+1]):
                    print("No one works well with the schedule")
                else:
                    print(self.day +self.time + "The schuedle might work?!")
    def print_members():
        GroupMember.print_schedule()
               
class GroupMember(Class):
    classSchedule=[sinfo,ainfo,kinfo]

    name=["Shirley","Aaron","Luke"]
    major=["ECE","ECE","System Engineering"]

    def __init__(self,name,major,classSchedule=[]):
        self.name=name
        self.major=major
        self.classSchedule=classSchedule

    def print_schedule(self):
        for i in range (1,4):
            print(name[i]+major[i]+classSchedule[i])
        


class Class():
    
    def __init__(self,departmnet,classNumber,startTime,endTime):
        self.department=department
        self.classNumber=classNumber
        self.startTime=startTime
        self.endTime=endTime

    def print_class_info(self):
        print("The class is " + department  + classNumber + " start from " + startTime + " to " + endTime)
sinfo=Class("ECE","3101",13.00,14.15)
ainfo=Class("ECE","3101",14.30,15.15)
einfo=Class("MAT","2240",18.00,19.15)
