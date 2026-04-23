from flask import Flask, request, jsonify, send_from_directory
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
app = Flask(__name__)
 
# ── Config ──────────────────────────────────────────
SENDER_EMAIL = "gannarholding@gmail.com"
SENDER_NAME  = "Pacific"
APP_PASSWORD  = "wtcm dhoe djpd bxjd"
SUBJECT      = "Regarding Hiring Manpower from Nepal"
 
# ── HTML Body ────────────────────────────────────────
HTML_BODY = """
<html>
<body style="font-family: Arial, sans-serif; max-width: 620px; margin: auto; color: #333; font-size: 15px; line-height: 1.7;">
  <div style="background-color: #003366; padding: 20px 30px; border-radius: 8px 8px 0 0;">
    <h1 style="color: #ffffff; margin: 0; font-size: 22px; letter-spacing: 1px;">PACIFIC HUMAN RESOURCES PVT. LTD.</h1>
    <p style="color: #a0c4e8; margin: 4px 0 0; font-size: 13px;">An ISO 9001:2008 Certified Agency | Est. 2005 | Kathmandu, Nepal</p>
  </div>
  <div style="background-color: #ffffff; padding: 30px; border: 1px solid #e0e0e0;">
    <p>Dear Sir/Madam,</p>
    <p>We are <strong>Pacific HR Pvt. Ltd.</strong>, an ISO-certified HR Management Company in Nepal, dedicated to delivering top-tier talent solutions. With <strong>19 years of experience</strong>, we specialize in identifying, screening, and placing professionals ranging from unskilled to highly skilled, tailored to your specific requirements.</p>
    <p><strong>Our services include:</strong></p>
    <table style="width: 100%; border-collapse: collapse;">
      <tr style="background-color: #f0f6ff;">
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7; width: 30px; font-weight: bold; color: #003366;">1</td>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7;"><strong>Swift Deployment</strong> – Candidates placed within <strong>10 days</strong>.</td>
      </tr>
      <tr>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7; font-weight: bold; color: #003366;">2</td>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7;"><strong>Experienced Workforce</strong> – Skilled professionals ready to contribute effectively.</td>
      </tr>
      <tr style="background-color: #f0f6ff;">
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7; font-weight: bold; color: #003366;">3</td>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7;"><strong>Flexible Agreements</strong> – Customizable contracts to align with your policies.</td>
      </tr>
      <tr>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7; font-weight: bold; color: #003366;">4</td>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7;"><strong>Visa Cost Commitment</strong> – We cover visa costs if a candidate is not deployed or does not complete two years.</td>
      </tr>
      <tr style="background-color: #f0f6ff;">
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7; font-weight: bold; color: #003366;">5</td>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7;"><strong>Pre-Deployment Training</strong> – We provide training in Nepal as per your instructions.</td>
      </tr>
    </table>
    <br>
    <p>We would be delighted to discuss your manpower requirements and explore a potential collaboration, under your terms and conditions for mutual benefits. Additionally, we invite you to <strong>visit Nepal</strong> and witness our commitment to excellence firsthand.</p>
    <p>Your kind consideration would be highly appreciated.</p>
    <br>
    <div style="border-top: 2px solid #003366; padding-top: 16px; margin-top: 10px;">
      <p style="margin: 0; font-weight: bold; font-size: 16px; color: #003366;">Ganga Kumari Pun</p>
      <p style="margin: 2px 0; font-size: 13px; color: #555;">Managing Director</p>
      <p style="margin: 10px 0 4px; font-size: 13px;">📱 <strong>WhatsApp / Mobile:</strong> <a href="https://wa.me/9779851019359" style="color: #003366;">+977-9851019359</a></p>
      <p style="margin: 2px 0; font-size: 13px;">✉️ <strong>Email:</strong> <a href="mailto:pacifichumanr@gmail.com" style="color: #003366;">pacifichumanr@gmail.com</a> | <a href="mailto:md@pacifichumanresources.com" style="color: #003366;">md@pacifichumanresources.com</a></p>
      <p style="margin: 2px 0; font-size: 13px;">🌐 <strong>Website:</strong> <a href="http://www.pacifichumanresources.com" style="color: #003366;">www.pacifichumanresources.com</a></p>
      <p style="margin: 2px 0; font-size: 13px;">📍 Samakhusi, Town Planning - 29, Kathmandu, Nepal</p>
      <div style="margin-top: 12px;">
        <a href="https://www.facebook.com" style="display: inline-block; margin-right: 8px; background-color: #1877F2; color: white; padding: 5px 14px; border-radius: 4px; text-decoration: none; font-size: 12px;">Facebook</a>
        <a href="https://www.linkedin.com" style="display: inline-block; margin-right: 8px; background-color: #0077B5; color: white; padding: 5px 14px; border-radius: 4px; text-decoration: none; font-size: 12px;">LinkedIn</a>
        <a href="https://www.youtube.com" style="display: inline-block; background-color: #FF0000; color: white; padding: 5px 14px; border-radius: 4px; text-decoration: none; font-size: 12px;">YouTube</a>
      </div>
    </div>
  </div>
  <div style="background-color: #f5f5f5; padding: 12px 30px; border: 1px solid #e0e0e0; border-top: none; border-radius: 0 0 8px 8px; text-align: center;">
    <p style="font-size: 11px; color: #999; margin: 0;">No. 64891/A/0001/UK/En (URS) &nbsp;|&nbsp; ISO 9001:2008 Certified &nbsp;|&nbsp; You received this email as a business contact.</p>
  </div>
</body>
</html>
"""
 
TEXT_BODY = """Dear Sir/Madam,
 
We are Pacific HR Pvt. Ltd., an ISO-certified HR Management Company in Nepal.
With 19 years of experience, we specialize in placing professionals tailored to your requirements.
 
Our services include:
1. Swift Deployment – Candidates placed within 10 days.
2. Experienced Workforce – Skilled professionals ready to contribute.
3. Flexible Agreements – Customizable contracts.
4. Visa Cost Commitment – We cover visa costs if needed.
5. Pre-Deployment Training – Training provided as per your instructions.
 
With Best Regards,
Ganga Kumari Pun
Managing Director
+977-9851019359
www.pacifichumanresources.com
"""
 
@app.route("/")
def index():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(base_dir, "index.html")
 
@app.route("/send", methods=["POST"])
def send_email():
    data = request.get_json()
    emails_raw = data.get("emails", "")
 
    # Parse comma or newline separated emails
    recipients = [e.strip() for e in emails_raw.replace("\n", ",").split(",") if e.strip()]
 
    if not recipients:
        return jsonify({"success": False, "message": "No valid email addresses provided."})
 
    success = []
    failed = []
 
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            for email in recipients:
                try:
                    msg = MIMEMultipart("alternative")
                    msg["Subject"] = SUBJECT
                    msg["From"]    = f"{SENDER_NAME} <{SENDER_EMAIL}>"
                    msg["To"]      = email
                    msg.attach(MIMEText(TEXT_BODY, "plain"))
                    msg.attach(MIMEText(HTML_BODY, "html"))
                    server.sendmail(SENDER_EMAIL, email, msg.as_string())
                    success.append(email)
                except Exception as e:
                    failed.append({"email": email, "error": str(e)})
    except Exception as e:
        return jsonify({"success": False, "message": f"SMTP connection failed: {str(e)}"})
 
    return jsonify({
        "success": True,
        "sent": len(success),
        "failed": len(failed),
        "successList": success,
        "failedList": failed
    })
 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
 
