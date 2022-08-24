from flask_app import app  # So we can run the app
# VERY IMPORTANT: ALWAYS import ALL of your controller files!
from flask_app.controllers import users, strategies


if __name__ == "__main__":  # Run the app
    app.run(debug=True)
