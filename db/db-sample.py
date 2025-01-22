import pymssql

conn = pymssql.connect(server='192.168.4.31', user='sa', password='Sakady0118', database='TypingSoft')
cursor = conn.cursor()
cursor.execute('SELECT code, text1, text2 FROM tbl_mondai_1')
row = cursor.fetchone()
while row:
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
    row = cursor.fetchone()
