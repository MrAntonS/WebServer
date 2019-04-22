from flask import Flask, session
from flask import render_template, redirect
from db_editor import DB, LetterModel, UsersModel
from forms import LoginForm, SignInForm, SendLetter
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'KEY'
database = 'FLASK.db'



def check():
    global current_session
    current_session = {}
    if "username" in session:
        current_session['username'] = session['username']
    if 'username' not in session:
        return True
    return False


@app.route('/')
@app.route('/index')
def index():
    if check(): return redirect('/login')
    users_model = UsersModel(db.get_connection())
    news_model = LetterModel(db.get_connection())
    news = news_model.get_all(session['username'])
    for a in range(len(news)):
        news[a] = list(news[a])
        news[a][4] = users_model.get_name(news[a][4])        
    return render_template('index.html', username=session['username'],
                           news=news, session=current_session, title="Главная")


@app.route('/login', methods=["GET", "POST"])
def login(): 
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_name = login_form.username.data
        password = login_form.password.data
        users_model = UsersModel(db.get_connection())
        
        pwd = users_model.get(user_name=user_name)
        if pwd and pwd[0]:
            if check_password_hash(pwd[2], password):
                session['username'] = user_name
                session['user_id'] = pwd[0]
        return redirect("/index")        
    return render_template('login.html', title='Авторизация', form=login_form)


@app.route('/logout')
def logout():
    session.pop('username',0)
    session.pop('user_id',0)
    return redirect('/login')
    

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    sign_in_form = SignInForm()
    if sign_in_form.validate_on_submit():
        user_name = sign_in_form.username.data
        password = generate_password_hash(sign_in_form.password.data)
        users_model = UsersModel(db.get_connection())
        if not users_model.get(user_name=user_name):
            
            user_id = users_model.insert(user_name, password)
            session['username'] = user_name
            session['user_id'] = user_id
            
            
            return redirect("/index") 
    return render_template("sign_in.html", title="Зарегестрироваться", form=sign_in_form)




@app.route("/send_letter", methods=["GET", "POST"])
def send_letter():
    if check(): return redirect('/login')
    
    letters_model = LetterModel(db.get_connection())
    letter_form = SendLetter()
    
    if letter_form.validate_on_submit():
        title = letter_form.title.data
        content = letter_form.content.data
        addressee = letter_form.addressee.data
        letters_model.insert(title, content, session['user_id'], addressee)
        return redirect("/index")
    return render_template("add_letter.html", title="Отправить письмо", form=letter_form, session=current_session)
  

@app.route("/del_letters")
def del_letters():
    if check(): return redirect('/login')
    user_model = UsersModel(db.get_connection())
    news_model = LetterModel(db.get_connection())
    news = news_model.get_all(session['username'])
    return render_template("del_letters.html", title="Удалить Письма", session=current_session, news=news)


@app.route("/del_letters/<int:letters_id>")
def del_letter(letters_id):
    if check(): return redirect('/login')
    letters_model = LetterModel(db.get_connection())
    user_model = UsersModel(db.get_connection())
    new = letters_model.get(letters_id)
    
    if new:
        authors_id = new[3]
        if session['username'] == authors_id:
            letters_model.delete(letters_id)
    return redirect("/del_letters")

@app.route("/read_letters/<int:letters_id>")
def read_letter(letters_id):
    if check(): return redirect('/login')
    letters_model = LetterModel(db.get_connection())
    user_model = UsersModel(db.get_connection())
    new = letters_model.get(letters_id)
    print(new)
    return render_template("read_letters.html", title="Удалить Письма", session=current_session, new=new)
def get_news(user_id):
    news_model = LettersModel(db.get_connection())
    news = list(map(lambda x: [user_id, x[1], x[2]],
                    letters_model.get_all(user_id)))
    return news


if __name__ == '__main__':
    db = DB(database)
    app.run(port=8080, host='0.0.0.0')
   
