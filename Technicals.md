Technically, following is all that is needed in the code.

#1. Connect to the Tally's ODBC interface.
#2. Definition and execution of queries.
#3. Extraction of data to excel files.

##Point 1.
Connection to Tally's ODBC is done through pyodbc library.
Code is just two lines. The 'DSN=' is default for 64bit installation of Tally with default ODBC driver port of 9000. IT can change it as required. But default should work just fine.

    import pyodbc
    
    cnxn = pyodbc.connect('DSN=TallyODBC64_9000;SERVER=({local});DRIVER=Tally ODBC DRIVER64;PORT=9000')

##Point 2.
Definition and execution of queries.
Following are some of the standard SQL queries with most used fields. I will keep them updating as more are needed. They are simply stores in a dict object, which anyone can modify and it will get updated.

    
    sql_strings_dict = {
    'Stock Items':'SELECT $Guid, $Name, $Parent, $Category, $Narration, $GSTTypeofSupply, $CostingMethod, $TreatPurchasesAsConsumed, $BaseUnits, $_LastPurcDate, $_LastPurcParty, $_LastPurcPrice, $_LastPurcCost, $_LastPurcQty, $OpeningBalance, $OpeningValue, $_InwardQuantity, $_InwardValue, $_OutwardQuantity, $_OutwardValue, $_ClosingBalance, $_ClosingValue FROM StockItem',

    'Stock Groups':'SELECT $Guid, $Name, $Parent, $CostingMethod, $BaseUnits, $IsAddable, $TreatPurchasesAsConsumed, $_ClosingBalance, $_ClosingValue FROM StockGroup',

    'Ledger Items':'SELECT $Guid, $Name, $Parent, $Narration, $IsBillWiseOn, $IsCostCenterOn, $IsCostTrackingOn, $AffectsStock, $SortPosition, $OpeningBalance, $_ClosingBalance, $_PrimaryGroup FROM LEDGER',

    'Ledger Groups':'SELECT $Guid, $Name, $Parent, $IsBillWiseOn, $IsCostCenterOn, $IsRevenue, $AffectsGrossProfit, $IsDeemedPositive, $AffectsStock, $SortPosition, $_PrimaryGroup, $_GrandParent, $_IsReserved, $_OpeningBalance, $_ClosingBalance FROM Groups',

    'Vendor Balances':'Select  $Name , $PARENT , $Narration, $ADDRESS[1].ADDRESS , $ADDRESS[2].ADDRESS , $ADDRESS[3].ADDRESS , $ADDRESS[4].ADDRESS , $ADDRESS[5].ADDRESS , $PINcode , $LEDSTATENAME , $CountryName , $LedgerContact , $MailingName , $LEDGERPHONE , $LEDGERMOBILE , $EMail , $PARTYGSTIN , $INCOMETAXNUMBER FROM LEDGER WHERE $_PrimaryGroup = "Sundry Creditors"',

    'Customer Balances':'Select  $Name , $PARENT , $Narration, $ADDRESS[1].ADDRESS , $ADDRESS[2].ADDRESS , $ADDRESS[3].ADDRESS , $ADDRESS[4].ADDRESS , $ADDRESS[5].ADDRESS , $PINcode , $LEDSTATENAME , $CountryName , $LedgerContact , $MailingName , $LEDGERPHONE , $LEDGERMOBILE , $EMail , $PARTYGSTIN , $INCOMETAXNUMBER FROM LEDGER WHERE $_PrimaryGroup = "Sundry Debtors"'
    }

Execution of queries is extremely simple with Pandas. Following will automatically fetch data from an open company in Tally.ERP9 on the local device and put it in a dataframe. sql_string is a text fetched from sql_string_dict.

    import pandas as pd
    df = pd.read_sql_query(sql_string,con=cnxn)
    
 
##Point 3
Extraction of Data to excel is a one line code. Pandas has lots of options which one can use (eg. create an writer object, preformat the dataframe and so forth.) But this is the simplest way of doing it. After this line of code, one can also call the filename and open it in Excel or other spreadsheet program.
    
    df.to_excel(filename+".xlsx")
