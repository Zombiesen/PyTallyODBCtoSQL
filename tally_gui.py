import tally_core as tc
import tally_customSQL as tq
import PySimpleGUI as sg

sql_string_dict = tc.sql_strings_dict
tq.import_sql(sql_string_dict)

def createGUI():
    layout = [  [sg.Text('PyTallyODBCtoSQL')],
                [sg.Text('Select the type of Report: '), sg.Combo(default_value='Stock Items', readonly=True, values=list(sql_string_dict.keys()))],
                [sg.Text('Save file as : '), sg.InputText(default_text='enter name of company here')],
                [sg.Button('Extract'), sg.Button('Exit')]
    ]

    window = sg.Window('PyTallyODBCtoSQL', layout, icon="icon.ico")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
            break
        if event == 'Extract':
            try:
                tc.extractData(values[0], values[0]+"-"+values[1])
                # ExecuteSQLString(SQLStringsDict.get(values[0]),values[0]+"-"+values[1])
            except Exception as e:
                sg.Popup('\n' + e, title='Warning..', custom_text='Ok', modal=True)
    window.close()


createGUI()
