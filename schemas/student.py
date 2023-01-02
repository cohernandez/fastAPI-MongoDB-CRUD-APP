# schemas to serialize and also convert mongoDB format json to our UI needed JSON

def studentEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "student_name":db_item["student_name"],
        "email":db_item["student_mail"],
        "phone":db_item["student_phone"]
    }

def listOfStudentEntity(db_item_list) -> list:
    list_student_entity = []
    for item in db_item_list:
        list_student_entity.append(studentEntity(item))
    return list_student_entity