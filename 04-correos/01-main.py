import imaplib
import email
from email.header import decode_header
import webbrowser
import os
from getpass import getpass

# Datos del usuario
username = input("Correo: ")
password = getpass("Password: ")

# Crear conexión
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# iniciar sesión
imap.login(username, password)

status, mensajes = imap.select("INBOX")
# print(mensajes)
# mensajes a recibir
N = 3
# cantidad total de correos
mensajes = int(mensajes[0])

for i in range(mensajes, mensajes - N, -1):
    # print(f"vamos por el mensaje: {i}")
#     # Obtener el mensaje
    try:
        res, mensaje = imap.fetch(str(i), "(RFC822)")
    except:
        break
    for respuesta in mensaje:
        if isinstance(respuesta, tuple):
            # Obtener el contenido
            mensaje = email.message_from_bytes(respuesta[1])
            # decodificar el contenido
            subject = decode_header(mensaje["Subject"])[0][0]
            if isinstance(subject, bytes):
                # convertir a string
                subject = subject.decode()
            # de donde viene el correo
            from_ = mensaje.get("From")
            print("Subject:", subject)
            print("From:", from_)
            print("Mensaje obtenido con exito")
            # si el correo es html
            if mensaje.is_multipart():
                # Recorrer las partes del correo
                for part in mensaje.walk():
                    # Extraer el contenido
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # el cuerpo del correo
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # Mostrar el cuerpo del correo
                        print(body)
                    elif "attachment" in content_disposition:
#                         # download attachment
                        nombre_archivo = part.get_filename()
                        if nombre_archivo:
                            if not os.path.isdir(subject):
                                # crear una carpeta para el mensaje
                                os.mkdir(subject)
                            ruta_archivo = os.path.join(subject, nombre_archivo)
                            # download attachment and save it
                            open(ruta_archivo, "wb").write(part.get_payload(decode=True))
            else:
                # contenido del mensaje
                content_type = mensaje.get_content_type()
                # cuerpo del mensaje
                body = mensaje.get_payload(decode=True).decode()
                if content_type == "text/plain":
#                     # mostrar solo el texto
                    print(body)
            # if content_type == "text/html":
            #     # Abrir el html en el navegador
            #     if not os.path.isdir(subject):
            #         os.mkdir(subject)
            #     nombre_archivo = f"{subject}.html"
            #     ruta_archivo = os.path.join(subject, nombre_archivo)
            #     open(ruta_archivo, "w").write(body)
            #     # abrir el navegador
            #     webbrowser.open(ruta_archivo)
#             print("********************************")
imap.close()
imap.logout()
