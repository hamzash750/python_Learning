import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=HAMZA\SQLEXPRESS;"
                      "Database=HeapStak;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM tbl_Product')

for row in cursor:
    print('row = %r' % (row,))