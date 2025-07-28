from app import app

# Expose the Flask app for Gunicorn
application = app.server

if __name__ == "__main__":
    app.run() 