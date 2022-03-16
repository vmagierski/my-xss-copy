from flask import Flask, render_template_string, render_template, request
import db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    search_query = request.args.get('q')

    comments = db.get_comments(search_query)

    return render_template('index.html',
                           comments=comments,
                           search_query=search_query)

@app.route("/ssti", methods=['GET'])
def home():
    name = request.args.get('name') or None; # get untrusted query param
    #return render_template_string(name); # render it into template
    return 'hi ' + name;
