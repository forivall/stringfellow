from flask import Flask, render_template
#from jinja2 import Environment
app = Flask(__name__)

#jenv = app.create_jinja_environment()

def yesno_filter(val):
    return 'yes' if val else 'no'
app.jinja_env.filters['yesno'] = yesno_filter

def updown_filter(val):
    return 'up' if val else 'down'
app.jinja_env.filters['updown'] = updown_filter

@app.route('/')
def root():
    return render_template('root.html', isup=True, serverstatuses=[])

if __name__ == '__main__':
    app.run(debug=True)
