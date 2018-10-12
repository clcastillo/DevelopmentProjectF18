# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:03:26 2018

@author: George
"""
    
class Course:
    def __init__(self, department, class_number, start_time, end_time):
        self.department = department
        self.class_number = class_number
        self.start_time = start_time
        self.end_time = end_time
        
    def obtain_class_info(self):
        return "Department: %s\nClass Number: %s\nStart time: %s\nEnd time: %s\n" % (self.department, self.class_number, self.start_time, self.end_time)

class GroupMember:
    def __init__(self, name, major, class_schedule):
        self.name = name
        self.major = major
        self.class_schedule = class_schedule
        
    def print_schedule(self):
        for course in self.class_schedule:
            print(course.obtain_class_info())
            
class Group_17:
    def __init__(self, group_members):
        self.group_members = group_members
    
    def meet_up(self, day, time):
        for member in self.group_members:
            for course in member.class_schedule:
                if((course.start_time <= time) & (course.end_time >= time)):
                    print("The meet time[%s at %s] obstructs with %s's %s course." % (day, time, member.name, course.class_number))
                    return False
                
        print("The meet time[%s at %s] works for all group members." % (day, time))
        return True
    
    def print_members(self):
        for member in self.group_members:
            print("Name: %s\nMajor: %s\n" % (member.name, member.major))
            member.print_schedule()

## testing
## my info
my_course_1 = Course('Electrical and Computer Engineering', '3250', '10:00', '11:15')
my_course_2 = Course('Electrical and Computer Engineering', '3300', '11:30', '12:45')
my_course_3 = Course('Electrical and Computer Engineering', '3300L', '13:00', '15:50')

my_class_schedule = [my_course_1, my_course_2, my_course_3]

member_1 = GroupMember('George', 'Electrical and Computer Engineering', my_class_schedule)


# group member 2
gm2_course_1 = Course('Computer Science', '2300', '09:00', '10:15')
gm2_course_2 = Course('Political Science', '1011', '13:00', '14:50')
gm2_course_3 = Course('Computer Science', '3210', '15:00', '16:15')

gm2_class_schedule = [gm2_course_1, gm2_course_2, gm2_course_3]

member_2 = GroupMember('Test Dummy 2', 'Computer Science', gm2_class_schedule)


## group member 3
gm3_course_1 = Course('Electrical and Computer Engineering', '4300', '17:30', '18:45')
gm3_course_2 = Course('Electrical and Computer Engineering', '4310', '16:00', '17:15')
gm3_course_3 = Course('Electrical and Computer Engineering', '3715', '13:00', '14:15')

gm3_class_schedule = [gm3_course_1, gm3_course_2, gm3_course_3]

member_3 = GroupMember('Test Dummy 3', 'Electrical and Computer Engineering', gm3_class_schedule)


my_group = [member_1, member_2, member_3]

my_group_17 = Group_17(my_group)

my_group_17.print_members()

## days aren't implemented properly because I'm lazy
group_meet = my_group_17.meet_up('Monday', '16:00')
group_meet = my_group_17.meet_up('Tuesday', '12:50')
group_meet = my_group_17.meet_up('Wednesday', '17:45')
group_meet = my_group_17.meet_up('Wednesday', '19:00')
group_meet = my_group_17.meet_up('Thursday', '12:50')
group_meet = my_group_17.meet_up('Friday', '11:00')
group_meet = my_group_17.meet_up('Friday', '13:30')