import smtplib, ssl
import getpass
import os
import pymysql
from email.message import EmailMessage

connection = pymysql.connect(
    host='aws.connect.psdb.cloud',  # Si es remota "ip"
    user='3upo4vz7ot99y168410o',
    port=3306,
    passwd='pscale_pw_GPwjNJGmlvQGcjW2UkKMdgOGNNsiDUScYapoOAZWPXW',
    db='athena_motors',
    ssl      = {
    "ca": "/etc/ssl/cert.pem"
  }
)
cursor = connection.cursor()

class class_mail:
    
    def mail(id, brand, line, year, vin, part_number, brand_part, price, product_Name):
        
        cursor.execute( 'SELECT *  FROM Person WHERE PersonID = "{}"'.format(id))
        result = cursor.fetchall()
        print(result)
        for i in result:
            info = i

        msg = EmailMessage()
        msg['Subject'] = 'Factura de apuesta de Athena.ai'
        msg['From'] = "athenaartificial@gmail.com"
        msg['to'] = info[5]
        msg.set_content('')
        msg.add_alternative(f"""\
                <!DOCTYPE html>
                <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
                <head>
                	<meta charset="UTF-8">
                	<meta name="viewport" content="width=device-width,initial-scale=1">
                	<meta name="x-apple-disable-message-reformatting">
                	<title></title>
                	<!--[if mso]>
                	<noscript>
                		<xml>
                			<o:OfficeDocumentSettings>
                				<o:PixelsPerInch>96</o:PixelsPerInch>
                			</o:OfficeDocumentSettings>
                		</xml>
                	</noscript>
                	<![endif]-->
                </head>
                <body style="margin:0;padding:0;">
                	<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
                		<tr>
                			<td align="center" style="padding:0;">
                				<table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
                					<tr>
                						<td align="center" style="padding:40px 0 30px 0;background: #000;">
                                            <h1 style="color: #c5b358;">ATHENA-Parts</h1>  
                						</td>
                					</tr>
                					<tr>
                						<td style="padding:36px 30px 42px 30px;">
                							<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                								<tr>
                									<td style="padding:0;">
                										<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                											<tr>
                												<td style="width:260px;padding:0;vertical-align:top;color: #000;;">
                													<p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Nombre: {info[2]} </p>
                                                                    <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Apellidos: {info[1]} </p>
                                                                    <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Id cliente: {info[0]}</p>
                                                                    <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Numero de orden: 1</p>
                												</td>
                												<td style="width:20px;padding:0;font-size:0;line-height:0;">&nbsp;</td>
                												<td style="width:260px;padding:0;vertical-align:top;color: #000;;">
                                                                    <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Marca: {brand}</p>
                                                                    <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Linea: {line}</p>
                                                                    <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Año: {year}</p>
                                                                    <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Precio: ${price}</p>
                												</td>
                                                                <td style="width:20px;padding:0;font-size:0;line-height:0;">&nbsp;</td>
                												<td style="width:260px;padding:0;vertical-align:top;color: #000;;">
                                                                    <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Refaccion: {product_Name}</p>
                                                                    <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Marca de la refaccion: {brand_part}</p>
                                                                    <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Numero de parte: {part_number}</p>
                												</td>
                											</tr>
                										</table>
                									</td>
                								</tr>
                							</table>
                						</td>
                					</tr>
                					<tr>
                						<td style="padding:30px;background: #000;;">
                							<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;font-size:9px;font-family:Arial,sans-serif;">
                								<tr>
                									<td style="padding:0;width:50%;" align="left">
                										<p style="margin:0;font-size:14px;line-height:16px;font-family:Arial,sans-serif;color:#ffffff;">
                											&reg; ATHENA-AI<br/><a href="http://www.example.com" style="color:#ffffff;text-decoration:underline;">PARTS</a>
                										</p>
                									</td>
                								</tr>
                							</table>
                						</td>
                					</tr>
                				</table>
                			</td>
                		</tr>
                	</table>
                </body>
                </html>
                """, subtype ='html')

        context=ssl.create_default_context()

        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as smtp:
            smtp.starttls(context=context)
            smtp.login(msg['From'], "HermesGod10")
            smtp.send_message(msg)
        exit()

