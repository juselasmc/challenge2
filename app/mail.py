import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(manager_email, owner_email, db_name):
    # Levantarlo
    smtp_server = smtplib.SMTP('miservidordecorreo.com', 587)
    smtp_server.starttls()
    smtp_server.login('compliance@miprogramita.co', 'mipassword')

    # Process
    msg = MIMEMultipart()
    msg['From'] = 'compliance@miprogramita.co'
    msg['To'] = manager_email
    msg['Cc'] = owner_email
    msg['Subject'] = "Database Classification Confirmation"

    # Body - Podria formaterse?
    body = f"Hola {owner_email} y {manager_email}, por favor confirmar que la {db_name} esta clasificada de manera correcta. Gracias"
    msg.attach(MIMEText(body, 'plain'))

    # Enviamos
    smtp_server.send_message(msg)
    del msg

    # Cerramos conexion SMTP server
    smtp_server.quit()
