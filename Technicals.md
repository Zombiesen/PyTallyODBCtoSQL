Technically, following is all that is needed in the code.

1. Connect to the Tally's ODBC interface.
2. Definition and execution of queries.
3. Extraction of data to excel files.

Point 1.
Connection to Tally's ODBC is done through pyodbc library.
Code is just two lines. The 'DSN=' is default for 64bit installation of Tally with default ODBC driver port of 9000. IT can change it as required. But default should work just fine.

_import pyodbc_
_cnxn = pyodbc.connect('DSN=TallyODBC64_9000;SERVER=({local});DRIVER=Tally ODBC DRIVER64;PORT=9000')_

Point 2.
Definition and execution of queries.
Following are some of the standard SQL queries with most used fields. I will keep them updating as more are needed. They are simply stores in a dict object, which anyone can modify and it will get updated.

_
SQLStringsDict = {
    'Stock Items':'SELECT $Guid, $Name, $Parent, $Category, $Narration, $GSTTypeofSupply, $CostingMethod, $TreatPurchasesAsConsumed, $BaseUnits, $_LastPurcDate, $_LastPurcParty, $_LastPurcPrice, $_LastPurcCost, $_LastPurcQty, $OpeningBalance, $OpeningValue, $_InwardQuantity, $_InwardValue, $_OutwardQuantity, $_OutwardValue, $_ClosingBalance, $_ClosingValue FROM StockItem',

    'Stock Groups':'SELECT $Guid, $Name, $Parent, $CostingMethod, $BaseUnits, $IsAddable, $TreatPurchasesAsConsumed, $_ClosingBalance, $_ClosingValue FROM StockGroup',

    'Ledger Items':'SELECT $Guid, $Name, $Parent, $Narration, $IsBillWiseOn, $IsCostCenterOn, $IsCostTrackingOn, $AffectsStock, $SortPosition, $OpeningBalance, $_ClosingBalance, $_PrimaryGroup FROM LEDGER',

    'Ledger Groups':'SELECT $Guid, $Name, $Parent, $IsBillWiseOn, $IsCostCenterOn, $IsRevenue, $AffectsGrossProfit, $IsDeemedPositive, $AffectsStock, $SortPosition, $_PrimaryGroup, $_GrandParent, $_IsReserved, $_OpeningBalance, $_ClosingBalance FROM Groups',

    'Vendor Balances':'Select  $Name , $PARENT , $Narration, $ADDRESS[1].ADDRESS , $ADDRESS[2].ADDRESS , $ADDRESS[3].ADDRESS , $ADDRESS[4].ADDRESS , $ADDRESS[5].ADDRESS , $PINcode , $LEDSTATENAME , $CountryName , $LedgerContact , $MailingName , $LEDGERPHONE , $LEDGERMOBILE , $EMail , $PARTYGSTIN , $INCOMETAXNUMBER FROM LEDGER WHERE $_PrimaryGroup = "Sundry Creditors"',

    'Customer Balances':'Select  $Name , $PARENT , $Narration, $ADDRESS[1].ADDRESS , $ADDRESS[2].ADDRESS , $ADDRESS[3].ADDRESS , $ADDRESS[4].ADDRESS , $ADDRESS[5].ADDRESS , $PINcode , $LEDSTATENAME , $CountryName , $LedgerContact , $MailingName , $LEDGERPHONE , $LEDGERMOBILE , $EMail , $PARTYGSTIN , $INCOMETAXNUMBER FROM LEDGER WHERE $_PrimaryGroup = "Sundry Debtors"'
}
_

