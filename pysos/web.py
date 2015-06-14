from pysos import app

if __name__ == '__main__':
    from pysos import settings

    if settings.DEBUG:
        app.run(debug=True, use_reloader=False)
    else:
        from logging.handlers import RotatingFileHandler

        file_handler = RotatingFileHandler(
            '/tmp/pysos.log', mode='a', maxBytes=2**20
        )
        file_handler.setLevel('DEBUG')
        app.logger.addHandler(file_handler)

        app.run(host='0.0.0.0', debug=False, use_reloader=False)
