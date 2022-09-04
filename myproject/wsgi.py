# This bit runs the whole operation in production environment
# TODO: Move it over to Gunicorn

from main import app

if __name__ == "__main__":
    app.run()
