from flask import Blueprint, render_template


home = Blueprint('', __name__)


@home.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@home.route('/login', methods=['POST'])
def login():
    pass


@home.route('/register', methods=['POST'])
def register():
    pass
