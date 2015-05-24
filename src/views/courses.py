from flask import Blueprint, render_template, request, flash
from flask.ext.login import current_user, login_required
from .forms import CourseForm
from models import Site, College


courses = Blueprint('courses', __name__)


@courses.route('/courses/new', methods=['GET'])
@login_required
def new_course():
    return render_template('newcourse.html', form=CourseForm())


@courses.route('/courses/new', methods=['POST'])
@login_required
def save_course():
    form = CourseForm()

    if not form.validate():
        return render_template('newcourse.html', form=form)

    try:
        College().register(form.name.data,
                           form.code.data.upper(),
                           form.teacher.data,
                           form.url.data)
        
        return redirect(url_for('home.index'))
    except Exception as error:
        flash(error)
        return render_template('newcourse.html', form=form)
