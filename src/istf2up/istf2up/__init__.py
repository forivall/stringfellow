from flask import Flask, render_template
app = Flask(__name__)

# CONFIG
app.config.from_object('defaultconfig.Default')
#app.config.from_envvar('ISTF2UP_SETTINGS')

# TEMPLATE FILTERS
@app.template_filter('yesno')
def yesno_filter(val):
    return 'yes' if val else 'no'

@app.template_filter('updown')
def updown_filter(val):
    return 'up' if val else 'down'

# ROUTES
@app.route('/')
def root():
    return render_template('root.html', isup=True, serverstatuses=[])

## LOGGING
#if not app.debug:
#    import logging
#    from logging.handlers import SMTPHandler
#    mail_handler = SMTPHandler('127.0.0.1',
#                               'server-error@istf2up.com',
#                               ADMINS, 'istf2up Failed')
#    mail_handler.setLevel(logging.ERROR)
#    mail_handler.setFormatter(logging.Formatter('''
#Message type:       %(levelname)s
#Location:           %(pathname)s:%(lineno)d
#Module:             %(module)s
#Function:           %(funcName)s
#Time:               %(asctime)s

#Message:

#%(message)s
#'''))
#    app.logger.addHandler(mail_handler)

if __name__ == '__main__':
    app.run()
