from rolepermissions.roles import AbstractUserRole
"""
Permissions are first ordered according to the acronym CRUD: 
    Create (Add), Read (View), Update (Edit), Delete,
    then in alphabetically.
"""

# TODO: Fix AbstractUserRole inheritance
"""
Permission don't seem to be inherited
"""


class CommonUser(AbstractUserRole):
    available_permissions = {
        'create_comment': True,
        'create_event': True,
        'create_guest': True,
        'create_post': True,

        'view_comment': True,
        'view_event': True,
        'view_guest': True,
        'view_post': True,

        'edit_comment': True,
        'edit_event': True,
        'edit_guest': True,
        'edit_post': True,

        'delete_comment': True,
        'delete_event': True,
        'delete_guest': True,
        'delete_post': True,
    }


class TeachingAssistant(CommonUser):
    available_permissions = {
        'create_assignment_file': True,
        'create_assignment_type': True,
        'create_gradebook_assignment_entry': True,
        'create_gradebook_note_entry': True,
        'create_lecture': True,
        'create_option': True,
        'create_question': True,

        'view_assignment': True,
        'view_assignment_file': True,
        'view_assignment_type': True,
        'view_course': True,
        'view_course_offering': True,
        'view_gradebook': True,
        'view_gradebook_assignment_entry': True,
        'view_gradebook_note_entry': True,
        'view_lecture': True,
        'view_option': True,
        'view_question': True,
        'view_study_plan': True,
        'view_waitlist': True,

        'edit_assignment': True,
        'edit_assignment_file': True,
        'edit_assignment_type': True,
        'edit_gradebook_assignment_entry': True,
        'edit_gradebook_note_entry': True,
        'edit_lecture': True,
        'edit_option': True,
        'edit_question': True,

        'delete_assignment_file': True,
        'delete_option': True,
        'delete_question': True,
    }


class Teacher(TeachingAssistant):
    """
    Teacher has the privileges of a Teaching Assistant + some more
    """
    available_permissions = {
        'create_assignment': True,
        'create_course': True,
        'create_course_offering': True,
        'create_study_plan': True,

        'edit_course': True,
        'edit_course_offering': True,
        'edit_gradebook': True,
        'edit_study_plan': True,

        'delete_assignment': True,
        'delete_assignment_type': True,
        'delete_course': True,
        'delete_course_offering': True,
        'delete_gradebook_assignment_entry': True,
        'delete_gradebook_note_entry': True,
        'delete_lecture': True,
        'delete_study_plan': True,
    }


class Student(CommonUser):
    available_permissions = {
        'create_enrollment': True,
        'create_file_submission': True,

        'view_assignment': True,
        'view_assignment_file': True,
        'view_assignment_type': True,
        'view_enrollment': True,
        'view_gradebook_assignment_entry': True,
        'view_gradebook_note_entry': True,
        'view_study_plan': True,
        'view_lecture': True,
        'view_option': True,
        'view_question': True,

        'edit_enrollment': True,
        'edit_file_submission': True,

        'delete_enrollment': True,
    }


class Writer(AbstractUserRole):
    available_permissions = {
        'create_comment': True,
        'create_post': True,

        'view_comment': True,
        'view_post': True,

        'edit_post': True,
        'edit_comment': True,

        'delete_comment': True,
        'delete_post': True,
    }


class Reviewer(AbstractUserRole):
    available_permissions = {
        'view_comment': True,
        'view_lecture': True,
        'view_post': True,
    }


class Moderator(Reviewer):
    available_permissions = {
        'delete_comment': True,
        'delete_lecture': True,
        'delete_post': True,
    }


class Editor(Moderator):
    available_permissions = {
        'edit_lecture': True,
        'edit_post': True,

        'delete_comment': False,
    }


class SystemAdmin(
    Moderator,
    Reviewer,
    Writer,
    Student,
    Teacher,
    TeachingAssistant
):
    pass
