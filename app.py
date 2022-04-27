from cgitb import html
from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample


app = Flask(__name__)
app.config['SECRET_KEY'] = "chickens"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
app.debug = True


@app.route('/root')
def homepage():
    return render_template('hello.html')
    
@app.route('/old')
def redirect_to_home():
    return redirect('/root')

@app.route('/hello')
def say_hello(name):
    return render_template('hello.html')

@app.route('/bye')
def say_goodbye():
    return "Goodbye!"

@app.route('/search')
def serach():
    term = request.args.get('term')
    sort = request.args.get('sort')
    print(request.args)
    return f"<h1>Searching...{term}</h1> <p>Sorting by: {sort}</p>"

@app.route("/add-comment", methods=['GET'])
def add_comment_form():
    return """
        <h1>Add Comment</h1>
        <form method ="POST">
            <input type="text" placeholder="Enter comment" name = 'comment'/>
            <input type="text" placeholder="Enter Usernname" name = 'user name'/>
            <button> Submit</button>
        </form>
    """

@app.route("/add-comment", methods=['POST'])
def save_comment():
    username = request.form["username"]
    comment = request.form["comment"]
    return f"""
        <h1> Saved your comment</h1>
        <ul>
            <li> Username: {username} </li>
            <li> Comment: {comment} </li>
        </ul>
    """

@app.route('/r/<subbreddit>')
def show_subreddit(subreddit):
    return f"<h1> Browse the {subreddit} Subbreddit"

@app.route('/r/<subreddit>comments/<int:post_id>')
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for post with {id} from the {subreddit} Subbreddit</h1>"

POSTS = {
    1: "I like chicken tenders",
    2: "Double rainbow",
    3:"I hate mayor",
    4: "YOLO"
}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, "Not found")
    return f"<p>{post}</p>"

@app.route('/lucky')
def lucky_number():
    num = randint(1,20)
    
    return render_template('lucky.html', lucky_num= num)

@app.route('/form')
def show_form():
    return render_template('form.html')

app.route('/form-2')
def show_form_2():
    return render_template('form2.html')


Compliments = ["Youre Cool", "Pythonic", "Amazing", "Incredible"]
@app.route('/greeter')
def get_greeting():
    username = request.args['username']
    nice_things = choice(Compliments)
    return render_template('greeting.html', username, compliment = nice_things)

@app.route('/greet-2')
def get_greeting_2():
    username = request.args['username']
    compliments = request.args.get["wants_compliments"]
    nice_things = sample(Compliments, 3)
    return render_template('greet2.html', username = username, wants_compliments = compliments, compliments = nice_things)

@app.route('/spell/ <word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell.html', word= caps_word)