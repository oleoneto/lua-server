# Specifies the directory to which the file will be uploaded
from django.utils import timezone
from datetime import timedelta
import textdistance


def assignment_submission_path(instance, filename):
    course_id = instance.assignment.course.id
    assignment_id = instance.assignment.id
    # Upload file to course_3435/assignment_101/files/submissions/<filename>
    return f'course_{course_id}/assignment_{assignment_id}/files/submissions'


def assignment_filepath(instance, filename):
    course_id = instance.assignment.course.id
    assignment_id = instance.assignment.id
    # Upload file to course_3435/assignment_101/files/<filename>
    return f'course_{course_id}/assignment_{assignment_id}/files'


def get_due_date():
    return timezone.now() + timedelta(weeks=1)


# TODO: Implement is_correct_answer()
def is_correct_answer(internal, external):
    textdistance.sorensen_dice.distance(internal, external)
    return False
