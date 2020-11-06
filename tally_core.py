import pyodbc
import pandas as pd

sql_strings_dict = {
    'Stock Items':'SELECT $Guid, $Name, $Parent, $Category, $Narration, $GSTTypeofSupply, $CostingMethod, $TreatPurchasesAsConsumed, $BaseUnits, $_LastPurcDate, $_LastPurcParty, $_LastPurcPrice, $_LastPurcCost, $_LastPurcQty, $OpeningBalance, $OpeningValue, $_InwardQuantity, $_InwardValue, $_OutwardQuantity, $_OutwardValue, $_ClosingBalance, $_ClosingValue FROM StockItem',
    'Stock Groups':'SELECT $Guid, $Name, $Parent, $CostingMethod, $BaseUnits, $IsAddable, $TreatPurchasesAsConsumed, $_ClosingBalance, $_ClosingValue FROM StockGroup',
    'Ledger Items':'SELECT $Guid, $Name, $Parent, $Narration, $IsBillWiseOn, $IsCostCenterOn, $IsCostTrackingOn, $AffectsStock, $SortPosition, $OpeningBalance, $_ClosingBalance, $_PrimaryGroup FROM LEDGER',
    'Ledger Groups':'SELECT $Guid, $Name, $Parent, $IsBillWiseOn, $IsCostCenterOn, $IsRevenue, $AffectsGrossProfit, $IsDeemedPositive, $AffectsStock, $SortPosition, $_PrimaryGroup, $_GrandParent, $_IsReserved, $_OpeningBalance, $_ClosingBalance FROM Groups',
    'Vendor Masters':'Select  $Name , $PARENT , $Narration, $ADDRESS[1].ADDRESS , $ADDRESS[2].ADDRESS , $ADDRESS[3].ADDRESS , $ADDRESS[4].ADDRESS , $ADDRESS[5].ADDRESS , $PINcode , $LEDSTATENAME , $CountryName , $LedgerContact , $MailingName , $LEDGERPHONE , $LEDGERMOBILE , $EMail , $PARTYGSTIN , $INCOMETAXNUMBER FROM LEDGER WHERE $_PrimaryGroup = "Sundry Creditors"',
    'Customer Masters':'Select  $Name , $PARENT , $Narration, $ADDRESS[1].ADDRESS , $ADDRESS[2].ADDRESS , $ADDRESS[3].ADDRESS , $ADDRESS[4].ADDRESS , $ADDRESS[5].ADDRESS , $PINcode , $LEDSTATENAME , $CountryName , $LedgerContact , $MailingName , $LEDGERPHONE , $LEDGERMOBILE , $EMail , $PARTYGSTIN , $INCOMETAXNUMBER FROM LEDGER WHERE $_PrimaryGroup = "Sundry Debtors"'
}

def extractData(report_name, file_name):
    '''

    '''
    try:
        cnxn = pyodbc.connect('DSN=TallyODBC64_9000;SERVER=({local});DRIVER=Tally ODBC DRIVER64;PORT=9000')
        df = pd.read_sql_query(sql_strings_dict.get(report_name),con=cnxn)
        df.to_excel(str(file_name)+".xlsx")
        return True
    except Exception as e:
        print(e)
        return False