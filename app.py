import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello Azure App Service! Flask is running."

@app.route("/health")
def health():
  return jsonify(
    status="ok",
    python=os.sys.version,
    app_service=os.environ.get("WEBSITE_SITE_NAME", "local"),
  )

if __name__ == "__main__":
  # ローカル実行用（Azureではgunicornが使われる）
  app.run(host="0.0.0.0", port=8000, debug=True)

