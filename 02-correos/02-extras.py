import smtplib, ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# pedir datos para iniciar de sesión
username = input("Ingrese su nombre de usuario: ")
password = getpass.getpass("Ingrese su password: ")

destinatario = input("Ingrese el destinatario: ")
asunto = input("Ingrese el asunto: ")

# Crear el mensaje
mensaje = MIMEMultipart("alternative") # estándar
mensaje["Subject"] = asunto
mensaje["From"] = username
mensaje["To"] = destinatario

html = f"""
<html>
<body>
    Hola <i>{destinatario}</i><br>
    Espero que estés <b>muy bien</b>
</body>
</html>
"""

# el contenido del mensaje como HTML
parte_html = MIMEText(html, "html")

# agregar ese contenido al mensaje
mensaje.attach(parte_html)

# enviar el mensaje
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username, password)
    print("Inicia sesion")
    server.sendmail(username, destinatario, mensaje.as_string())
    print("mensaje enviado")

