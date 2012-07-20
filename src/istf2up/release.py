import istf2up
istf2up.app.config.from_object('defaultconfig.Release')
app = istf2up.app.wsgi_app
#if __name__ == '__main__':
#    istf2up.app.run()
