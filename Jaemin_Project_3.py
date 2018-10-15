class Group_6:

    def __init__(self):
        self.time = ""
        self.day = ""
        self.names = ["Jaemin", "Jose", "Kobe", "Wilson"]

    def meet_up(self, time, day):
        print("Group members can meet " + str(self.time) + str(self.day))

    def print_members(self):
        print(self.names, self.majors, self.class_schedule)


class GroupMember:
    def __init__(self, name, major, class_schedule = []):
        self.name = name
        self.major = major
        self.class_schedule = class_schedule

    def print(self):
        print("Name: " + str(self.name))
        print("Major: " + str(self.major))
        print("Class Schedule")
        x = len(self.class_schedule)
        for i in range(x):
            print(self.class_schedule[i])


class Class:
    def __init__ (self, department, class_number, day, start_time, end_time):
        self.department = department
        self.classNumber = class_number
        self.startTime = start_time
        self.endTime = end_time
        self.day = day

    def print_class_info(self):
        print("Department: " + Class.department)
        print("Class number: " + Class.classNumber)
        print("Day: " + Class.day)
        print("Start time: " + Class.startTime)
        print("End time: " + Class.endTime)

class main:
    Jaemin_1 = Class("ECE", "1101", "TTH", "2:30", "3:45")
    Jaemin_2 = Class("ECE", "1301", "MW", "8:00", "9:45")
    Jaemin_3 = Class("ECE", "1101L", "TH", "7:00", "9:45")
    Jaemin_4 = Class("MAT", "2240", "TTH", "8:30", "9:45")
    Jaemin_5 = Class("CHM", "1210", "TTH", "5:30", "6:45")
    Jaemin_6 = Class("CHM", "1210L", "F", "8:00", "10:45")
    Jaemin.class_schedule = [Jaemin_1, Jaemin_2, Jaemin_3, Jaemin_4, Jaemin_5, Jaemin_6]

    teamList[Jaemin.class_schedule, Jose.class_schedule, Kobe.class_schedule, Wilson.class_schedule]
