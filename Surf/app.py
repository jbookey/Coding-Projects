from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Surf Application in Progress! Thanks, Jack"

if __name__ == "__main__":
    # Enable debug mode for development (auto-restarts on code changes)
    app.run(debug=True)

