from logging.config import dictConfig

from status.app import app

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s[%(levelname)s]%(module)s:%(lineno)s: %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
