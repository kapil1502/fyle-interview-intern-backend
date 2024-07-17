from flask import Blueprint
from core.apis import decorators
from core.apis.teachers.schema import TeacherSchema
from core.models.teachers import Teacher
from core.apis.responses import APIResponse

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)

@principal_teachers_resources.route('/', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of assignments"""
    principal_teachers = Teacher.get_teachers_by_principal(p.principal_id)
    principal_teachers_dump = TeacherSchema().dump(principal_teachers, many=True)
    return APIResponse.respond(data=principal_teachers_dump)