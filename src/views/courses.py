from flask.ext.login import current_user, login_required
from flask import Blueprint, render_template, request
from .forms import CourseForm
from models import Site


courses = Blueprint('courses', __name__)


@courses.route('/courses/new', methods=['GET'])
@login_required
def new_course():
    return render_template('newcourse.html', form=CourseForm())


@courses.route('/courses/new', methods=['POST'])
@login_required
def save_course():
    pass
