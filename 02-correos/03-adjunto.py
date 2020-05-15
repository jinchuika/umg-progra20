import smtplib, ssl
import getpass

from email import encoders
from email.mime.base import MIMEBase
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
    Hola {destinatario}<br>
    Te mando esta imagen <b>muy bonita</b> :D
</body>
</html>
"""
# el contenido del mensaje como HTML
parte_html = MIMEText(html, "html")
# agregar ese contenido al mensaje
mensaje.attach(parte_html)

# ruta del archivo
archivo = "imagen.jpg"
# leer el archivo
with open(archivo, "rb") as adjunto:
    # crear el contenido de tipo Base
    contenido_adjunto = MIMEBase("application", "octet-stream")
    # adjuntar el archivo al contenido base
    contenido_adjunto.set_payload(adjunto.read())

# codificar ese contenido
encoders.encode_base64(contenido_adjunto)
# agregar encabezados
contenido_adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename= {archivo}",
)
# agregar / adjuntar ese contenido al mensaje
mensaje.attach(contenido_adjunto)
mensaje_final = mensaje.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username, password)
    print("sesion iniciada")
    server.sendmail(username, destinatario, mensaje_final)
    print("mensaje enviado")

