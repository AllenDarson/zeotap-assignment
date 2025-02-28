#Code for Chatbot (Flask)#
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple documentation storage (can be expanded)#
cdp_docs = {
    "segment": "To set up a source in Segment, go to Sources > Add Source...",
    "mparticle": "To create a user profile in mParticle, navigate to Users > Profiles...",
    "lytics": "To build an audience in Lytics, go to Audiences > Create Audience...",
    "zeotap": "To integrate data in Zeotap, go to Integrations > Add Integration...",
}

@app.route("/chatbot", methods=["POST"])
def chatbot():
    query = request.json.get("query", "").lower()
    
    for key in cdp_docs:
        if key in query:
            return jsonify({"response": cdp_docs[key]})
    
    return jsonify({"response": "I could not find an answer. Please check the official documentation."})

if __name__ == "__main__":
    app.run(debug=True)
