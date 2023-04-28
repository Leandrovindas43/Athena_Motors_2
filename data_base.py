import pymysql
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


#connection = MySQLdb.connect(
#  host= os.getenv("HOST"),
#  user=os.getenv("USERNAME"),
#  passwd= os.getenv("PASSWORD"),
#  db= os.getenv("DATABASE"),
#  ssl_mode = "VERIFY_IDENTITY",
#  ssl      = {
#    "ca": "/etc/ssl/cert.pem"
#  }
#)
cursor = connection.cursor()
cursor.execute(
    'SELECT Brand, Line, Year, PlateCar, Vim  FROM Cars WHERE PlateCar = "{}"'.format(85639))
result = cursor.fetchall()
print(result)