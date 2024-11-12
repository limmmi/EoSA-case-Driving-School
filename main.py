para={
    "studentNum" : 25,
    "InstructorNum":2,
    "vehicleNum":4,

}

# initialize the lesson plan
oneLesson={"lessonID":0,
           "type":'',
           "studentID":[],
           "instructorID":0,
           "date":'2022-01-01',
           "time":'10:00-12:00',
           "completed":"completed",
           "canBeBooked":"No",
           "pay":0}

# initialize vehicle information
vehicleInfo={"vehicleID":0,
             "type":'car',
             "needMaintenance":False}

# initialize instructor information
instructorInfo={"instructorID":0,
                "name":'',
                "gender":'male',
                "age":30,
                "salary":5000,
                "lessons":[],
                "income":0}

# initialize student information
studentInfo={"studentID":0,
             "name":'',
             "gender":'male',
             "age":18,
             "lessons":[],
             "unpaid":0}

# initialize payment information
paymentInfo={"paymentID":0,
             "studentID":0,
             "amount":0,
             "lessonID":0,
             "status":'unpaid'}


