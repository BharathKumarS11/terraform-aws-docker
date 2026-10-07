from flask import Flask  # type: ignore[import-not-found]

app = Flask(__name__)

@app.route("/")
def home():
    return "Terraform AWS Docker Project - Version 1"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)