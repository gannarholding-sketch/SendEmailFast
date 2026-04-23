import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ── Config ──────────────────────────────────────────
SENDER_EMAIL = "gannarholding@gmail.com"
SENDER_NAME  = "Pacific"
APP_PASSWORD  = "wtcm dhoe djpd bxjd"   # Gmail App Password

SUBJECT = "Regarding Hiring Manpower from Nepal"

# ── Recipient list ───────────────────────────────────
recipients = [
    "gannarholding@gmail.com",
    "iamsimant24@gmail.com"
]

# ── Email body (HTML) ────────────────────────────────
HTML_BODY = """
<html>
<body style="font-family: Arial, sans-serif; max-width: 620px; margin: auto; color: #333; font-size: 15px; line-height: 1.7;">

  <!-- Header Banner -->
  <div style="background-color: #003366; padding: 20px 30px; border-radius: 8px 8px 0 0;">
    <h1 style="color: #ffffff; margin: 0; font-size: 22px; letter-spacing: 1px;">PACIFIC HUMAN RESOURCES PVT. LTD.</h1>
    <p style="color: #a0c4e8; margin: 4px 0 0; font-size: 13px;">An ISO 9001:2008 Certified Agency | Est. 2005 | Kathmandu, Nepal</p>
  </div>

  <!-- Body -->
  <div style="background-color: #ffffff; padding: 30px; border: 1px solid #e0e0e0;">

    <p>Dear Sir/Madam,</p>

    <p>
      We are <strong>Pacific HR Pvt. Ltd.</strong>, an ISO-certified HR Management Company in Nepal, 
      dedicated to delivering top-tier talent solutions. With <strong>19 years of experience</strong>, 
      we specialize in identifying, screening, and placing professionals ranging from unskilled to 
      highly skilled, tailored to your specific requirements.
    </p>

    <p><strong>Our services include:</strong></p>

    <table style="width: 100%; border-collapse: collapse;">
      <tr style="background-color: #f0f6ff;">
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7; width: 30px; font-weight: bold; color: #003366;">1</td>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7;">
          <strong>Swift Deployment</strong> – Candidates placed within <strong>10 days</strong>.
        </td>
      </tr>
      <tr>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7; font-weight: bold; color: #003366;">2</td>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7;">
          <strong>Experienced Workforce</strong> – Skilled professionals ready to contribute effectively.
        </td>
      </tr>
      <tr style="background-color: #f0f6ff;">
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7; font-weight: bold; color: #003366;">3</td>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7;">
          <strong>Flexible Agreements</strong> – Customizable contracts to align with your policies.
        </td>
      </tr>
      <tr>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7; font-weight: bold; color: #003366;">4</td>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7;">
          <strong>Visa Cost Commitment</strong> – We cover visa costs if a candidate is not deployed or does not complete two years.
        </td>
      </tr>
      <tr style="background-color: #f0f6ff;">
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7; font-weight: bold; color: #003366;">5</td>
        <td style="padding: 10px 14px; border: 1px solid #d0e4f7;">
          <strong>Pre-Deployment Training</strong> – We provide training in Nepal as per your instructions.
        </td>
      </tr>
    </table>

    <br>
    <p>
      We would be delighted to discuss your manpower requirements and explore a potential collaboration, 
      under your terms and conditions for mutual benefits. Additionally, we invite you to 
      <strong>visit Nepal</strong> and witness our commitment to excellence firsthand.
    </p>

    <p>Your kind consideration would be highly appreciated.</p>

    <br>

    <!-- Signature -->
    <div style="border-top: 2px solid #003366; padding-top: 16px; margin-top: 10px;">
      <p style="margin: 0; font-weight: bold; font-size: 16px; color: #003366;">Ganga Kumari Pun</p>
      <p style="margin: 2px 0; font-size: 13px; color: #555;">Managing Director</p>

      <p style="margin: 10px 0 4px; font-size: 13px;">
        📱 <strong>WhatsApp / Mobile:</strong> 
        <a href="https://wa.me/9779851019359" style="color: #003366;">+977-9851019359</a>
      </p>
      <p style="margin: 2px 0; font-size: 13px;">
        ✉️ <strong>Email:</strong>
        <a href="mailto:pacifichumanr@gmail.com" style="color: #003366;">pacifichumanr@gmail.com</a> | 
        <a href="mailto:md@pacifichumanresources.com" style="color: #003366;">md@pacifichumanresources.com</a>
      </p>
      <p style="margin: 2px 0; font-size: 13px;">
        🌐 <strong>Website:</strong> 
        <a href="http://www.pacifichumanresources.com" style="color: #003366;">www.pacifichumanresources.com</a>
      </p>
      <p style="margin: 2px 0; font-size: 13px;">
        📍 Samakhusi, Town Planning - 29, Kathmandu, Nepal
      </p>

      <!-- Social Links -->
      <div style="margin-top: 12px;">
        <a href="#" style="display: inline-block; margin-right: 8px; background-color: #1877F2; color: white; padding: 5px 14px; border-radius: 4px; text-decoration: none; font-size: 12px;">Facebook</a>
        <a href="#" style="display: inline-block; margin-right: 8px; background-color: #0077B5; color: white; padding: 5px 14px; border-radius: 4px; text-decoration: none; font-size: 12px;">LinkedIn</a>
        <a href="#" style="display: inline-block; background-color: #FF0000; color: white; padding: 5px 14px; border-radius: 4px; text-decoration: none; font-size: 12px;">YouTube</a>
      </div>
    </div>

  </div>

  <!-- Footer -->
  <div style="background-color: #f5f5f5; padding: 12px 30px; border: 1px solid #e0e0e0; border-top: none; border-radius: 0 0 8px 8px; text-align: center;">
    <p style="font-size: 11px; color: #999; margin: 0;">
      No. 64891/A/0001/UK/En (URS) &nbsp;|&nbsp; ISO 9001:2008 Certified &nbsp;|&nbsp; 
      You received this email as a business contact.
    </p>
  </div>

</body>
</html>
"""

# ── Plain text fallback ──────────────────────────────
TEXT_BODY = """
Dear Sir/Madam,



We are Pacific HR Pvt. Ltd., an ISO-certified HR Management Company in Nepal, dedicated to delivering top-tier talent solutions. 

With 19 years of experience, we specialize in identifying, screening, and placing professionals ranging from unskilled to highly skilled, tailored to your specific requirements.

Our services include:

Swift Deployment – Candidates placed within 10 days.
Experienced Workforce – Skilled professionals ready to contribute effectively.
Flexible Agreements – Customizable contracts to align with your policies.
Visa Cost Commitment – We cover visa costs if a candidate is not deployed or does not complete two years.
Pre-Deployment Training – We provide training in Nepal as per your instructions.

We would be delighted to discuss your manpower requirements and explore a potential collaboration, under your terms and conditions for mutual benefits.  Additionally, we invite you to visit Nepal and witness our commitment to excellence firsthand. 

Your kind consideration would be highly appreciated. 



With Best Regards,

Ganga Kumari Pun

Managing Director

Whatsapp/Mobile:- 00977-9851019359

E-mail: pacifichumanr@gmail.com

md@pacifichumanresources.com
PACIFIC HUMAN RESOURCES PVT. LTD.
Samakhusi, Town Planning - 29 Kathmandu - Nepal
An ISO 9001:2008 Certified Agency
No. 64891/A/0001/UK/En (URS)
             
URL:   www.pacifichumanresources.com
Follow us:   Facebook   Linkedin    Youtube
"""

# ── Send emails ──────────────────────────────────────
def send_newsletter(recipients):
    success = 0
    failed  = []

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)

        for email in recipients:
            try:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = SUBJECT
                msg["From"]    = f"{SENDER_NAME} <{SENDER_EMAIL}>"
                msg["To"]      = email  # only their own address visible

                msg.attach(MIMEText(TEXT_BODY, "plain"))  # fallback

                server.sendmail(SENDER_EMAIL, email, msg.as_string())
                print(f"✅ Sent to {email}")
                success += 1

            except Exception as e:
                print(f"❌ Failed for {email}: {e}")
                failed.append(email)

    print(f"\nDone! {success} sent, {len(failed)} failed.")
    if failed:
        print("Failed addresses:", failed)

# ── Run ──────────────────────────────────────────────
send_newsletter(recipients)