import os
import tempfile
from flask import Flask, request, render_template_string
from document_reader import DocumentReader
from qa_engine import QAEngine

app = Flask(__name__)

FORM_HTML = """
<!doctype html>
<title>Document QA</title>
<h1>Ask a question</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file accept=".pdf,.docx,.txt,.xlsx" required>
  <input type=text name=question placeholder="Your question" required>
  <input type=submit value=Ask>
</form>
{% if answer %}
<h2>Answer</h2>
<pre>{{answer}}</pre>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        f = request.files.get("file")
        q = request.form.get("question", "")
        if f and q:
            tmp = tempfile.NamedTemporaryFile(delete=False)
            f.save(tmp.name)
            reader = DocumentReader()
            texts = reader.read(tmp.name)
            engine = QAEngine(texts)
            answer = engine.ask(q)
            os.unlink(tmp.name)
    return render_template_string(FORM_HTML, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
