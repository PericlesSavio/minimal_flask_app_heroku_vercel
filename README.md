# A minimal Flask application for Heroku and Vercel.

## Heroku
requirements.txt

    flask
    gevent
    gunicorn

Procfile

    web: gunicorn app:app

## Vercel
requirements.txt

    flask
    gevent
    gunicorn

vercel.json

    {
        "version": 2,
        "builds": [{
            "src": "./app.py",
            "use": "@vercel/python"
        }],
        "routes": [{
            "src": "/(.*)",
            "dest": "/app.py"
        }]
    }
