Technically, following is all that is needed in the code.

1. Connect to the Tally's ODBC interface.
2. Definition and execution of queries.
3. Extraction of data to excel files.

1. Connection to Tally's ODBC is done through pyodbc library.
Code is just two lines. The 'DSN=' is default for 64bit installation of Tally with default ODBC driver port of 9000. IT can change it as required. But default should work just fine.

import pyodbc
cnxn = pyodbc.connect('DSN=TallyODBC64_9000;SERVER=({local});DRIVER=Tally ODBC DRIVER64;PORT=9000')

