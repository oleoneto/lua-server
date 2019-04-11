import bson


def make_student_id():
    return bson.objectid.ObjectId()
