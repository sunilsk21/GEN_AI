from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# 🔑 Paste your Gemini API key here
genai.configure(api_key="AIzaSyD9OESOSbu7SbL49MSRRPOe6p31vGqyvIM")

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    email_text = ""
    if request.method == "POST":
        purpose = request.form["purpose"]
        tone = request.form["tone"]
        recipient = request.form["recipient"]

        prompt = f"""
        Write a professional email.
        Purpose: {purpose}
        Tone: {tone}
        Recipient: {recipient}
        """

        response = model.generate_content(prompt)
        email_text = response.text

    return render_template("index.html", email=email_text)

if __name__ == "__main__":
    app.run(debug=True)
