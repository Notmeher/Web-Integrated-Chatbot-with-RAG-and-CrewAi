from flask import Flask, request, jsonify, render_template
from crew import crew_workflow

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.json.get("query", "")
    if not user_query:
        return jsonify({"error": "No question provided"}), 400
    
    try:
        result = crew_workflow(user_query)
        
        if "error" in result:
            return jsonify({"error": result["error"]})
        
        response = result.get("response", {})
        answer = response.get("result", "No answer provided.")
        return jsonify({"question": user_query, "answer": answer})
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
