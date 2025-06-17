from flask import Flask, request, jsonify, send_file
import openai
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


def generate_pdf(text: str) -> io.BytesIO:
    """Generate a simple PDF with the provided text."""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    text_obj = c.beginText(50, height - 50)
    text_obj.setFont("Helvetica", 12)
    for line in text.splitlines():
        text_obj.textLine(line)
    c.drawText(text_obj)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer


@app.route("/webhook", methods=["POST"])
def receive_webhook():
    """Receive resume data from Tally and return an enhanced PDF."""
    print("📥 Webhook HIT")

    try:
        data = request.get_json(force=True)
    except Exception as exc:
        print("❌ JSON Error:", exc)
        return jsonify({"error": "Invalid JSON", "details": str(exc)}), 400

    full_name = data.get("First and last name", "N/A")
    experience = data.get("Past experience", "")
    job_target = data.get("job title/internship target", "")

    prompt = (
        f"My name is {full_name}. I am targeting a position as a {job_target}.\n"
        f"My past experience: {experience}\n"
        "Please rewrite my experience to make it sound more professional, "
        "structured, and ATS-friendly."
    )

    print("➡️ Prompt sent to GPT:\n", prompt)

    try:
        gpt_response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert resume writer."},
                {"role": "user", "content": prompt},
            ],
        )
        enhanced_content = gpt_response["choices"][0]["message"]["content"]
    except Exception as exc:
        print("❌ GPT Error:", exc)
        return jsonify({"error": "OpenAI API failed", "details": str(exc)}), 500

    print("✅ Enhanced Content Generated")

    pdf_buffer = generate_pdf(enhanced_content)

    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name=f"{full_name.replace(' ', '_')}_resume.pdf",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
