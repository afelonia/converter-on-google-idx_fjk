import flet as ft
from flet import *

def main (page: ft.Page):
    # page.window.always_on_top=True
    page.window.resizable=True

    page.window.visible=True
    # page.window.frameless=True
    page.window.center=True
    page.title="myConverter"

   

    # USER INPUT FOR VALUE TO BE CONVERTED
    userinput=TextField(value=1,label='value to convert',bgcolor="#B0B0B0",width=200,text_align=TextAlign.CENTER,autofocus=True,keyboard_type=KeyboardType.NUMBER,adaptive=True,label_style=TextStyle(size=18,weight=FontWeight.BOLD),)
    userinputValue=userinput.value
    # CHECK VALIDITY FOR USER INPUT4
    def checkField(e):
        try:
            float(userinput.value)
            userinput.color=colors.BLACK
            userinput.border_color=colors.BLACK
            # page.update()
        except ValueError:
            userinput.color='red'
            userinput.border_color='red'
            

        page.update()

    userinput.on_change=checkField
    page.update()



# ?SELECTION LISTS
    lengthList={
        'in':0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
        'mm': 0.001,
        'cm': 0.01,
        'm':1,
        'km': 1000,
    }


    areaList={
        'in\u00b2':0.00064516,
        'ft\u00b2': 0.09290304,
        'yd\u00b2': 0.83612736,
        'mi\u00b2': 2589988.110336,
        'ac': 4046.8564224,
        'ha':10000,
        'mm\u00b2': 0.000001,
        'cm\u00b2': 0.0001,
        'm\u00b2':1,
        'km\u00b2': 1000000,
    }
    volumeList={
        'ft\u00b3': 0.028316847,
        'in\u00b3':1.63871E-05,
        'cm\u00b3': 0.000001,
        'm\u00b3':1,
        'mi\u00b3': 4168181825,
        'yd\u00b3': 0.764554858,
    }

    # print(format(list(areaList.values())[7],","))
    # print(format(list(areaList.keys())))
    # print(f"in2ft: {in2ft}")
    # print(f"ft2in: {ft2in}")

# SELECTION OF THE TYPE TO DEAL WITH I.E DIST,AREA OR VOLUME
    txtType=['length'.capitalize(),'area'.capitalize(),'volume'.capitalize()]
    def radioSelected(e):
        value=e.control.value
        if value==txtType[0]:
            fromLengthDropdown.options=[dropdown.Option(option) for option in list(lengthList.keys())]
            toLengthDropdown.options=[dropdown.Option(option) for option in list(lengthList.keys())]
            fromLengthDropdown.update()
            toLengthDropdown.update()

        elif value==txtType[1]:
            fromLengthDropdown.options=[dropdown.Option(option) for option in list(areaList.keys())]
            toLengthDropdown.options=[dropdown.Option(option) for option in list(areaList.keys())]
            fromLengthDropdown.update()
            toLengthDropdown.update()
        else:
            fromLengthDropdown.options=[dropdown.Option(option) for option in list(volumeList.keys())]
            toLengthDropdown.options=[dropdown.Option(option) for option in list(volumeList.keys())]
            page.update()
            fromLengthDropdown.update()
            toLengthDropdown.update()

    type_radio=RadioGroup(
        value=txtType[1],
        content=Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Radio(value=txtType[0],label=txtType[0],label_position='left'),
                Radio(value=txtType[1],label=txtType[1],label_position='left'),
                Radio(value=txtType[2],label=txtType[2],label_position='left'),
            ]
        ),
        on_change=radioSelected,
    )


    typeContainer=Container(
        content=Column(
            [
                type_radio,
]
        )
    )
# LENGTH DROPDOWN
    fromLengthDropdown=Dropdown(
        width=100,
        padding=padding.only(top=0,bottom=0),
        label="From",
        value=list(areaList.keys())[8],
        label_style=TextStyle(weight=FontWeight.W_200,color=colors.ORANGE),
        options=[
            dropdown.Option(choice) for choice in list(areaList.keys())
            ],      
            # on_change=compute,
    )
    toLengthDropdown=Dropdown(
        width=100,
        padding=padding.only(top=0,bottom=0),
        label="To",
        value=list(areaList.keys())[8],
        label_style=TextStyle(weight=FontWeight.W_200,color=colors.ORANGE),
        options=[
            dropdown.Option(choice) for choice in list(areaList.keys())
            ]
        
    )
    
    # FROMTXT=0,TOTXT=1
    val0,val1=str(list(lengthList.keys())[0]),str(list(lengthList.keys())[1])
    val2,val3=str(list(lengthList.keys())[2]),str(list(lengthList.keys())[3])
    val4,val5=str(list(lengthList.keys())[4]),str(list(lengthList.keys())[5])
    val6,val7=str(list(lengthList.keys())[6]),str(list(lengthList.keys())[7])

    area0,area1=str(list(areaList.keys())[0]),str(list(areaList.keys())[1])
    area2,area3=str(list(areaList.keys())[2]),str(list(areaList.keys())[3])
    area4,area5=str(list(areaList.keys())[4]),str(list(areaList.keys())[5])
    area6,area7=str(list(areaList.keys())[6]),str(list(areaList.keys())[7])
    area8,area9=str(list(areaList.keys())[8]),str(list(areaList.keys())[9])
# COMPUTE THE RESULT
# COMPUTE THE RESULT
    # in2ft=list(lengthList.values())[0]/list(lengthList.values())[1]
    # ft2in=1/in2ft
    def compute(e):
        try:
            userinputValue=float(userinput.value)
            outputField.update()

            if fromLengthDropdown.value==toLengthDropdown.value:
                # print(f'{userinput.value} {fromLengthDropdown.value}')
                # print(in2ft)
                outputField.value=userinput.value
                page.update()

                """...................................DISTANCE CONVERSION...............................
                ........................................................................................
                ........................................................................................
                ."""
                # CONVERSION OF INCH TO ANY....................................................................
                # TO FEET 
            elif fromLengthDropdown.value==val0 and toLengthDropdown.value==str(list(lengthList.keys())[1]):
                outputField.value=in2ft=format(round(userinputValue*list(lengthList.values())[0]/list(lengthList.values())[1],8),",")
                outputField.update()
                # TO YARD
            elif fromLengthDropdown.value==val0 and toLengthDropdown.value==str(list(lengthList.keys())[2]):
                outputField.value=in2yd=format(userinputValue*list(lengthList.values())[0]/list(lengthList.values())[2],",")
                outputField.update()
                # TO MILE
            elif fromLengthDropdown.value==val0 and toLengthDropdown.value==str(list(lengthList.keys())[3]):
                outputField.value=in2mi=format(userinputValue*list(lengthList.values())[0]/list(lengthList.values())[3],",")
                outputField.update()
                # TO MILIMETER
            elif fromLengthDropdown.value==val0 and toLengthDropdown.value==str(list(lengthList.keys())[4]):
                outputField.value=in2mm=format(userinputValue*list(lengthList.values())[0]/list(lengthList.values())[4],",")
                outputField.update()
                # TO CENTIMETER
            elif fromLengthDropdown.value==val0 and toLengthDropdown.value==str(list(lengthList.keys())[5]):
                outputField.value=in2cm=format(userinputValue*list(lengthList.values())[0]/list(lengthList.values())[5],",")
                outputField.update()
                # TO METER
            elif fromLengthDropdown.value==val0 and toLengthDropdown.value==str(list(lengthList.keys())[6]):
                outputField.value=in2m=format(userinputValue*list(lengthList.values())[0]/list(lengthList.values())[6],",")
                outputField.update()
                # TO KILOMETER
            elif fromLengthDropdown.value==val0 and toLengthDropdown.value==str(list(lengthList.keys())[7]):
                outputField.value=in2km=format(round(userinputValue*list(lengthList.values())[0]/list(lengthList.values())[7]),",")
                outputField.update()

                # FROM FOOT TO ANY ....................................................................

            elif fromLengthDropdown.value==val1 and toLengthDropdown.value==str(list(lengthList.keys())[0]):
                outputField.value=ft2in=format(userinputValue*list(lengthList.values())[1]/list(lengthList.values())[0],",")
                outputField.update()
                # TO YARD
            elif fromLengthDropdown.value==val1 and toLengthDropdown.value==str(list(lengthList.keys())[2]):
                outputField.value=ft2yd=format(userinputValue*list(lengthList.values())[1]/list(lengthList.values())[2],",")
                outputField.update()
                # TO MILE
            elif fromLengthDropdown.value==val1 and toLengthDropdown.value==str(list(lengthList.keys())[3]):
                outputField.value=ft2mi=format(userinputValue*list(lengthList.values())[1]/list(lengthList.values())[3],",")
                outputField.update()
                # TO MILIMETER
            elif fromLengthDropdown.value==val1 and toLengthDropdown.value==str(list(lengthList.keys())[4]):
                outputField.value=ft2mm=format(userinputValue*list(lengthList.values())[1]/list(lengthList.values())[4],",")
                outputField.update()
                # TO CENTIMETER
            elif fromLengthDropdown.value==val1 and toLengthDropdown.value==str(list(lengthList.keys())[5]):
                outputField.value=ft2cm=format(userinputValue*list(lengthList.values())[1]/list(lengthList.values())[5],",")
                outputField.update()
                # TO METER
            elif fromLengthDropdown.value==val1 and toLengthDropdown.value==str(list(lengthList.keys())[6]):
                outputField.value=ft2m=format(userinputValue*list(lengthList.values())[1]/list(lengthList.values())[6],",")
                outputField.update()
                # TO KILOMETER
            elif fromLengthDropdown.value==val1 and toLengthDropdown.value==str(list(lengthList.keys())[7]):
                outputField.value=ft2km=format(userinputValue*list(lengthList.values())[1]/list(lengthList.values())[7],",")
                outputField.update()
                # TO 

                # FROM YARD TO ANY .......................................................................
            elif fromLengthDropdown.value==val2 and toLengthDropdown.value==str(list(lengthList.keys())[0]):
                outputField.value=yd2in=format(userinputValue*list(lengthList.values())[2]/list(lengthList.values())[0],",")
                outputField.update()
                # TO FEET
            elif fromLengthDropdown.value==val2 and toLengthDropdown.value==str(list(lengthList.keys())[1]):
                outputField.value=yd2ft=format(userinputValue*list(lengthList.values())[2]/list(lengthList.values())[1],",")
                outputField.update()
                # TO MILE
            elif fromLengthDropdown.value==val2 and toLengthDropdown.value==str(list(lengthList.keys())[3]):
                outputField.value=yd2mi=format(userinputValue*list(lengthList.values())[2]/list(lengthList.values())[3],",")
                outputField.update()
                # TO MILIMETER
            elif fromLengthDropdown.value==val2 and toLengthDropdown.value==str(list(lengthList.keys())[4]):
                outputField.value=yd2mm=format(userinputValue*list(lengthList.values())[2]/list(lengthList.values())[4],",")
                outputField.update()
                # TO CENTIMETER
            elif fromLengthDropdown.value==val2 and toLengthDropdown.value==str(list(lengthList.keys())[5]):
                outputField.value=yd2cm=format(userinputValue*list(lengthList.values())[2]/list(lengthList.values())[5],",")
                outputField.update()
                # TO METER
            elif fromLengthDropdown.value==val2 and toLengthDropdown.value==str(list(lengthList.keys())[6]):
                outputField.value=yd2m=format(userinputValue*list(lengthList.values())[2]/list(lengthList.values())[6],",")
                outputField.update()
                # TO KILOMETER
            elif fromLengthDropdown.value==val2 and toLengthDropdown.value==str(list(lengthList.keys())[7]):
                outputField.value=yd2km=format(userinputValue*list(lengthList.values())[2]/list(lengthList.values())[7],",")
                outputField.update()
                # TO 
                # FROM MILE TO ANY ...................................................................
                # TO INCH
            elif fromLengthDropdown.value==val3 and toLengthDropdown.value==str(list(lengthList.keys())[0]):
                outputField.value=mile2mi=format(userinputValue*list(lengthList.values())[3]/list(lengthList.values())[0],",")
                outputField.update()
                # TO FEET
            elif fromLengthDropdown.value==val3 and toLengthDropdown.value==str(list(lengthList.keys())[1]):
                outputField.value=mile2ft=format(userinputValue*list(lengthList.values())[3]/list(lengthList.values())[1],",")
                outputField.update()
                # TO YARD
            elif fromLengthDropdown.value==val3 and toLengthDropdown.value==str(list(lengthList.keys())[2]):
                outputField.value=mile2yd=format(userinputValue*list(lengthList.values())[3]/list(lengthList.values())[2],",")
                outputField.update()
                # TO MILIMETER
            elif fromLengthDropdown.value==val3 and toLengthDropdown.value==str(list(lengthList.keys())[4]):
                outputField.value=mile2mm=format(userinputValue*list(lengthList.values())[3]/list(lengthList.values())[4],",")
                outputField.update()
                # TO CENTIMETER
            elif fromLengthDropdown.value==val3 and toLengthDropdown.value==str(list(lengthList.keys())[5]):
                outputField.value=mile2cm=format(userinputValue*list(lengthList.values())[3]/list(lengthList.values())[5],",")
                outputField.update()
                # TO METER
            elif fromLengthDropdown.value==val3 and toLengthDropdown.value==str(list(lengthList.keys())[6]):
                outputField.value=mile2m=format(userinputValue*list(lengthList.values())[3]/list(lengthList.values())[6],",")
                outputField.update()
                # TO KILOMETER
            elif fromLengthDropdown.value==val3 and toLengthDropdown.value==str(list(lengthList.keys())[7]):
                outputField.value=mile2km=format(userinputValue*list(lengthList.values())[3]/list(lengthList.values())[7],",")
                outputField.update()

                # FROM MILIMETER TO ANY ..............................................................
                # TO inch
            elif fromLengthDropdown.value==val4 and toLengthDropdown.value==str(list(lengthList.keys())[0]):
                outputField.value=mm2mm=format(userinputValue*list(lengthList.values())[4]/list(lengthList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==val4 and toLengthDropdown.value==str(list(lengthList.keys())[1]):
                outputField.value=mm2ft=format(userinputValue*list(lengthList.values())[4]/list(lengthList.values())[1],",")
                outputField.update()
                # TO YARD
            elif fromLengthDropdown.value==val4 and toLengthDropdown.value==str(list(lengthList.keys())[2]):
                outputField.value=mmyd=format(userinputValue*list(lengthList.values())[4]/list(lengthList.values())[2],",")
                outputField.update()
                # TO MILE
            elif fromLengthDropdown.value==val4 and toLengthDropdown.value==str(list(lengthList.keys())[3]):
                outputField.value=mm2mi=format(userinputValue*list(lengthList.values())[4]/list(lengthList.values())[3],",")
                outputField.update()
                # TO CENTIMETER
            elif fromLengthDropdown.value==val4 and toLengthDropdown.value==str(list(lengthList.keys())[5]):
                outputField.value=mm2cm=format(userinputValue*list(lengthList.values())[4]/list(lengthList.values())[5],",")
                outputField.update()
                # TO METER
            elif fromLengthDropdown.value==val4 and toLengthDropdown.value==str(list(lengthList.keys())[6]):
                outputField.value=mm2m=format(userinputValue*list(lengthList.values())[4]/list(lengthList.values())[6],",")
                outputField.update()
                # TO KILOMETER
            elif fromLengthDropdown.value==val4 and toLengthDropdown.value==str(list(lengthList.keys())[7]):
                outputField.value=mm2km=format(userinputValue*list(lengthList.values())[4]/list(lengthList.values())[7],",")
                outputField.update()
            

                # FROM CENTIMETER TO ANY .............................................................
                # TO inch
            elif fromLengthDropdown.value==val5 and toLengthDropdown.value==str(list(lengthList.keys())[0]):
                outputField.value=cm2cm=format(userinputValue*list(lengthList.values())[5]/list(lengthList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==val5 and toLengthDropdown.value==str(list(lengthList.keys())[1]):
                outputField.value=cm2ft=format(userinputValue*list(lengthList.values())[5]/list(lengthList.values())[1],",")
                outputField.update()
                # TO YARD
            elif fromLengthDropdown.value==val5 and toLengthDropdown.value==str(list(lengthList.keys())[2]):
                outputField.value=cm2yd=format(userinputValue*list(lengthList.values())[5]/list(lengthList.values())[2],",")
                outputField.update()
                # TO MILE
            elif fromLengthDropdown.value==val5 and toLengthDropdown.value==str(list(lengthList.keys())[3]):
                outputField.value=cm2mi=format(userinputValue*list(lengthList.values())[5]/list(lengthList.values())[3],",")
                outputField.update()
                # TO MILIMETER
            elif fromLengthDropdown.value==val5 and toLengthDropdown.value==str(list(lengthList.keys())[4]):
                outputField.value=cm2mm=format(userinputValue*list(lengthList.values())[5]/list(lengthList.values())[4],",")
                outputField.update()
                # TO METER
            elif fromLengthDropdown.value==val5 and toLengthDropdown.value==str(list(lengthList.keys())[6]):
                outputField.value=cm2m=format(userinputValue*list(lengthList.values())[5]/list(lengthList.values())[6],",")
                outputField.update()
                # TO KILOMETER
            elif fromLengthDropdown.value==val5 and toLengthDropdown.value==str(list(lengthList.keys())[7]):
                outputField.value=cm2km=format(userinputValue*list(lengthList.values())[5]/list(lengthList.values())[7],",")
                outputField.update()


                # FROM METER TO ANY .............................................................
                # TO inch
            elif fromLengthDropdown.value==val6 and toLengthDropdown.value==str(list(lengthList.keys())[0]):
                outputField.value=m2cm=float(format(userinputValue*list(lengthList.values())[6]/list(lengthList.values())[0],","))
                outputField.update()
            elif fromLengthDropdown.value==val6 and toLengthDropdown.value==str(list(lengthList.keys())[1]):
                outputField.value=m2ft=format(userinputValue*list(lengthList.values())[6]/list(lengthList.values())[1],",")
                outputField.update()
                # TO YARD
            elif fromLengthDropdown.value==val6 and toLengthDropdown.value==str(list(lengthList.keys())[2]):
                outputField.value=m2yd=format(userinputValue*list(lengthList.values())[6]/list(lengthList.values())[2],",")
                outputField.update()
                # TO MILE
            elif fromLengthDropdown.value==val6 and toLengthDropdown.value==str(list(lengthList.keys())[3]):
                outputField.value=m2mi=format(userinputValue*list(lengthList.values())[6]/list(lengthList.values())[3],",")
                outputField.update()
                # TO MILIMETER
            elif fromLengthDropdown.value==val6 and toLengthDropdown.value==str(list(lengthList.keys())[4]):
                outputField.value=m2mm=format(userinputValue*list(lengthList.values())[6]/list(lengthList.values())[4],",")
                outputField.update()
                # TO CENTIMETER
            elif fromLengthDropdown.value==val6 and toLengthDropdown.value==str(list(lengthList.keys())[5]):
                outputField.value=m2mm=format(userinputValue*list(lengthList.values())[6]/list(lengthList.values())[5],",")
                outputField.update()
                # TO KILOMETER
            elif fromLengthDropdown.value==val6 and toLengthDropdown.value==str(list(lengthList.keys())[7]):
                outputField.value=m2km=format(userinputValue*list(lengthList.values())[6]/list(lengthList.values())[7],",")
                outputField.update()



                # FROM KILOMETER TO ANY .............................................................
                # TO inch
            elif fromLengthDropdown.value==val7 and toLengthDropdown.value==str(list(lengthList.keys())[0]):
                outputField.value=km2cm=format(userinputValue*list(lengthList.values())[7]/list(lengthList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==val7 and toLengthDropdown.value==str(list(lengthList.keys())[1]):
                outputField.value=km2ft=format(userinputValue*list(lengthList.values())[7]/list(lengthList.values())[1],",")
                outputField.update()
                # TO YARD
            elif fromLengthDropdown.value==val7 and toLengthDropdown.value==str(list(lengthList.keys())[2]):
                outputField.value=kmyd=format(userinputValue*list(lengthList.values())[7]/list(lengthList.values())[2],",")
                outputField.update()
                # TO MILE
            elif fromLengthDropdown.value==val7 and toLengthDropdown.value==str(list(lengthList.keys())[3]):
                outputField.value=km2mi=format(userinputValue*list(lengthList.values())[7]/list(lengthList.values())[3],",")
                outputField.update()
                # TO MILIMETER
            elif fromLengthDropdown.value==val7 and toLengthDropdown.value==str(list(lengthList.keys())[4]):
                outputField.value=km2mm=format(userinputValue*list(lengthList.values())[7]/list(lengthList.values())[4],",")
                outputField.update()
                # TO CENTIMETER
            elif fromLengthDropdown.value==val7 and toLengthDropdown.value==str(list(lengthList.keys())[5]):
                outputField.value=cm2km=format(userinputValue*list(lengthList.values())[7]/list(lengthList.values())[5],",")
                outputField.update()
                # TO METER
            elif fromLengthDropdown.value==val7 and toLengthDropdown.value==str(list(lengthList.keys())[6]):
                outputField.value=km2m=format(userinputValue*list(lengthList.values())[7]/list(lengthList.values())[6],",")
                outputField.update()

                

                """ ...................AREA CONVERSION..............."""

                """ ...................FROM SQUARE INCH..............."""

            elif fromLengthDropdown.value==area0 and toLengthDropdown.value==str(list(areaList.keys())[1]):
                outputField.value=sq_inTo_sq_ft=format(userinputValue*list(areaList.values())[0]/list(areaList.values())[1],",")
                outputField.update()
            elif fromLengthDropdown.value==area0 and toLengthDropdown.value==str(list(areaList.keys())[2]):
                outputField.value=sq_inTo_sq_yd=format(userinputValue*list(areaList.values())[0]/list(areaList.values())[2],",")
                outputField.update()
            elif fromLengthDropdown.value==area0 and toLengthDropdown.value==str(list(areaList.keys())[3]):
                outputField.value=sq_inTo_sq_mile=format(userinputValue*list(areaList.values())[0]/list(areaList.values())[3],",")
                outputField.update()
            elif fromLengthDropdown.value==area0 and toLengthDropdown.value==str(list(areaList.keys())[4]):
                outputField.value=sq_inTo_sq_acres=format(userinputValue*list(areaList.values())[0]/list(areaList.values())[4],",")
                outputField.update()
            elif fromLengthDropdown.value==area0 and toLengthDropdown.value==str(list(areaList.keys())[5]):
                outputField.value=sq_inTo_sq_hectares=format(userinputValue*list(areaList.values())[0]/list(areaList.values())[5],",")
                outputField.update()
            elif fromLengthDropdown.value==area0 and toLengthDropdown.value==str(list(areaList.keys())[6]):
                outputField.value=sq_inTo_sq_milimeters=format(userinputValue*list(areaList.values())[0]/list(areaList.values())[6],",")
                outputField.update()
            elif fromLengthDropdown.value==area0 and toLengthDropdown.value==str(list(areaList.keys())[7]):
                outputField.value=sq_inTo_sq_centimeters=format(userinputValue*list(areaList.values())[0]/list(areaList.values())[7],",")
                outputField.update()
            elif fromLengthDropdown.value==area0 and toLengthDropdown.value==str(list(areaList.keys())[8]):
                outputField.value=sq_inTo_sq_meters=format(userinputValue*list(areaList.values())[0]/list(areaList.values())[8],",")
                outputField.update()
            elif fromLengthDropdown.value==area0 and toLengthDropdown.value==str(list(areaList.keys())[9]):
                outputField.value=sq_inTo_sq_kilometers=format(userinputValue*list(areaList.values())[0]/list(areaList.values())[9],",")
                outputField.update()




                """ ...................FROM SQUARE FEET..............."""

            elif fromLengthDropdown.value==area1 and toLengthDropdown.value==str(list(areaList.keys())[0]):
                outputField.value=sq_feetTo_sq_inch=format(userinputValue*list(areaList.values())[1]/list(areaList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==area1 and toLengthDropdown.value==str(list(areaList.keys())[2]):
                outputField.value=sq_feetTo_sq_yd=format(userinputValue*list(areaList.values())[1]/list(areaList.values())[2],",")
                outputField.update()
            elif fromLengthDropdown.value==area1 and toLengthDropdown.value==str(list(areaList.keys())[3]):
                outputField.value=sq_feetTo_sq_mile=format(userinputValue*list(areaList.values())[1]/list(areaList.values())[3],",")
                outputField.update()
            elif fromLengthDropdown.value==area1 and toLengthDropdown.value==str(list(areaList.keys())[4]):
                outputField.value=sq_feetTo_sq_acres=format(userinputValue*list(areaList.values())[1]/list(areaList.values())[4],",")
                outputField.update()
            elif fromLengthDropdown.value==area1 and toLengthDropdown.value==str(list(areaList.keys())[5]):
                outputField.value=sq_feetTo_sq_hectares=format(userinputValue*list(areaList.values())[1]/list(areaList.values())[5],",")
                outputField.update()
            elif fromLengthDropdown.value==area1 and toLengthDropdown.value==str(list(areaList.keys())[6]):
                outputField.value=sq_feetTo_sq_milimeters=format(userinputValue*list(areaList.values())[1]/list(areaList.values())[6],",")
                outputField.update()
            elif fromLengthDropdown.value==area1 and toLengthDropdown.value==str(list(areaList.keys())[7]):
                outputField.value=sq_feetTo_sq_centimeters=format(userinputValue*list(areaList.values())[1]/list(areaList.values())[7],",")
                outputField.update()
            elif fromLengthDropdown.value==area1 and toLengthDropdown.value==str(list(areaList.keys())[8]):
                outputField.value=sq_feetTo_sq_meters=format(userinputValue*list(areaList.values())[1]/list(areaList.values())[8],",")
                outputField.update()
            elif fromLengthDropdown.value==area1 and toLengthDropdown.value==str(list(areaList.keys())[9]):
                outputField.value=sq_feetTo_sq_kilometers=format(userinputValue*list(areaList.values())[1]/list(areaList.values())[9],",")
                outputField.update()


                """ ...................FROM SQUARE YARD..............."""

            elif fromLengthDropdown.value==area2 and toLengthDropdown.value==str(list(areaList.keys())[0]):
                outputField.value=sq_YardTo_sq_inch=format(userinputValue*list(areaList.values())[2]/list(areaList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==area2 and toLengthDropdown.value==str(list(areaList.keys())[1]):
                outputField.value=sq_YardTo_sq_feet=format(userinputValue*list(areaList.values())[2]/list(areaList.values())[1],",")
                outputField.update()
            elif fromLengthDropdown.value==area2 and toLengthDropdown.value==str(list(areaList.keys())[3]):
                outputField.value=sq_YardTo_sq_mile=format(userinputValue*list(areaList.values())[2]/list(areaList.values())[3],",")
                outputField.update()
            elif fromLengthDropdown.value==area2 and toLengthDropdown.value==str(list(areaList.keys())[4]):
                outputField.value=sq_YardTo_sq_acres=format(userinputValue*list(areaList.values())[2]/list(areaList.values())[4],",")
                outputField.update()
            elif fromLengthDropdown.value==area2 and toLengthDropdown.value==str(list(areaList.keys())[5]):
                outputField.value=sq_YardTo_sq_hectares=format(userinputValue*list(areaList.values())[2]/list(areaList.values())[5],",")
                outputField.update()
            elif fromLengthDropdown.value==area2 and toLengthDropdown.value==str(list(areaList.keys())[6]):
                outputField.value=sq_YardTo_sq_milimeters=format(userinputValue*list(areaList.values())[2]/list(areaList.values())[6],",")
                outputField.update()
            elif fromLengthDropdown.value==area2 and toLengthDropdown.value==str(list(areaList.keys())[7]):
                outputField.value=sq_YardTo_sq_centimeters=format(userinputValue*list(areaList.values())[2]/list(areaList.values())[7],",")
                outputField.update()
            elif fromLengthDropdown.value==area2 and toLengthDropdown.value==str(list(areaList.keys())[8]):
                outputField.value=sq_YardTo_sq_meters=format(userinputValue*list(areaList.values())[2]/list(areaList.values())[8],",")
                outputField.update()
            elif fromLengthDropdown.value==area2 and toLengthDropdown.value==str(list(areaList.keys())[9]):
                outputField.value=sq_YardTo_sq_kilometers=format(userinputValue*list(areaList.values())[2]/list(areaList.values())[9],",")
                outputField.update()



                """ ...................FROM SQUARE MILE..............."""

            elif fromLengthDropdown.value==area3 and toLengthDropdown.value==str(list(areaList.keys())[0]):
                outputField.value=sq_MileTo_sq_inch=format(userinputValue*list(areaList.values())[3]/list(areaList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==area3 and toLengthDropdown.value==str(list(areaList.keys())[1]):
                outputField.value=sq_MileTo_sq_feet=format(userinputValue*list(areaList.values())[3]/list(areaList.values())[1],",")
                outputField.update()
            elif fromLengthDropdown.value==area3 and toLengthDropdown.value==str(list(areaList.keys())[2]):
                outputField.value=sq_MileTo_sq_Yard=format(userinputValue*list(areaList.values())[3]/list(areaList.values())[2],",")
                outputField.update()
            elif fromLengthDropdown.value==area3 and toLengthDropdown.value==str(list(areaList.keys())[4]):
                outputField.value=sq_MileTo_sq_acres=format(userinputValue*list(areaList.values())[3]/list(areaList.values())[4],",")
                outputField.update()
            elif fromLengthDropdown.value==area3 and toLengthDropdown.value==str(list(areaList.keys())[5]):
                outputField.value=sq_MileTo_sq_hectares=format(userinputValue*list(areaList.values())[3]/list(areaList.values())[5],",")
                outputField.update()
            elif fromLengthDropdown.value==area3 and toLengthDropdown.value==str(list(areaList.keys())[6]):
                outputField.value=sq_MileTo_sq_milimeters=format(userinputValue*list(areaList.values())[3]/list(areaList.values())[6],",")
                outputField.update()
            elif fromLengthDropdown.value==area3 and toLengthDropdown.value==str(list(areaList.keys())[7]):
                outputField.value=sq_MileTo_sq_centimeters=format(userinputValue*list(areaList.values())[3]/list(areaList.values())[7],",")
                outputField.update()
            elif fromLengthDropdown.value==area3 and toLengthDropdown.value==str(list(areaList.keys())[8]):
                outputField.value=sq_MileTo_sq_meters=format(userinputValue*list(areaList.values())[3]/list(areaList.values())[8],",")
                outputField.update()
            elif fromLengthDropdown.value==area3 and toLengthDropdown.value==str(list(areaList.keys())[9]):
                outputField.value=sq_MileTo_sq_kilometers=format(userinputValue*list(areaList.values())[3]/list(areaList.values())[9],",")
                outputField.update()


                """ ...................FROM  ACRES..............."""

            elif fromLengthDropdown.value==area4 and toLengthDropdown.value==str(list(areaList.keys())[0]):
                outputField.value=acresTo_sq_inch=format(userinputValue*list(areaList.values())[4]/list(areaList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==area4 and toLengthDropdown.value==str(list(areaList.keys())[1]):
                outputField.value=acresTo_sq_feet=format(userinputValue*list(areaList.values())[4]/list(areaList.values())[1],",")
                outputField.update()
            elif fromLengthDropdown.value==area4 and toLengthDropdown.value==str(list(areaList.keys())[2]):
                outputField.value=acresTo_sq_Yard=format(userinputValue*list(areaList.values())[4]/list(areaList.values())[2],",")
                outputField.update()
            elif fromLengthDropdown.value==area4 and toLengthDropdown.value==str(list(areaList.keys())[3]):
                outputField.value=acresTo_sq_Miles=format(userinputValue*list(areaList.values())[4]/list(areaList.values())[3],",")
                outputField.update()
            elif fromLengthDropdown.value==area4 and toLengthDropdown.value==str(list(areaList.keys())[5]):
                outputField.value=acresTo_sq_hectares=format(userinputValue*list(areaList.values())[4]/list(areaList.values())[5],",")
                outputField.update()
            elif fromLengthDropdown.value==area4 and toLengthDropdown.value==str(list(areaList.keys())[6]):
                outputField.value=acresTo_sq_milimeters=format(userinputValue*list(areaList.values())[4]/list(areaList.values())[6],",")
                outputField.update()
            elif fromLengthDropdown.value==area4 and toLengthDropdown.value==str(list(areaList.keys())[7]):
                outputField.value=acresTo_sq_centimeters=format(userinputValue*list(areaList.values())[4]/list(areaList.values())[7],",")
                outputField.update()
            elif fromLengthDropdown.value==area4 and toLengthDropdown.value==str(list(areaList.keys())[8]):
                outputField.value=acresTo_sq_meters=format(userinputValue*list(areaList.values())[4]/list(areaList.values())[8],",")
                outputField.update()
            elif fromLengthDropdown.value==area4 and toLengthDropdown.value==str(list(areaList.keys())[9]):
                outputField.value=acresTo_sq_kilometers=format(userinputValue*list(areaList.values())[4]/list(areaList.values())[9],",")
                outputField.update()
                """ ...................FROM   HECTACRES..............."""

            elif fromLengthDropdown.value==area5 and toLengthDropdown.value==str(list(areaList.keys())[0]):
                outputField.value=sq_hectaresTo_sq_inch=format(userinputValue*list(areaList.values())[5]/list(areaList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==area5 and toLengthDropdown.value==str(list(areaList.keys())[1]):
                outputField.value=sq_hectaresTo_sq_feet=format(userinputValue*list(areaList.values())[5]/list(areaList.values())[1],",")
                outputField.update()
            elif fromLengthDropdown.value==area5 and toLengthDropdown.value==str(list(areaList.keys())[2]):
                outputField.value=sq_hectaresTo_sq_Yard=format(userinputValue*list(areaList.values())[5]/list(areaList.values())[2],",")
                outputField.update()
            elif fromLengthDropdown.value==area5 and toLengthDropdown.value==str(list(areaList.keys())[4]):
                outputField.value=sq_hectaresTo_sq_acres=format(userinputValue*list(areaList.values())[5]/list(areaList.values())[4],",")
                outputField.update()
            elif fromLengthDropdown.value==area5 and toLengthDropdown.value==str(list(areaList.keys())[3]):
                outputField.value=sq_hectaresTo_sq_miles=format(userinputValue*list(areaList.values())[4]/list(areaList.values())[3],",")
                outputField.update()
            elif fromLengthDropdown.value==area5 and toLengthDropdown.value==str(list(areaList.keys())[6]):
                outputField.value=sq_hectaresTo_sq_milimeters=format(userinputValue*list(areaList.values())[5]/list(areaList.values())[6],",")
                outputField.update()
            elif fromLengthDropdown.value==area5 and toLengthDropdown.value==str(list(areaList.keys())[7]):
                outputField.value=sq_hectaresTo_sq_centimeters=format(userinputValue*list(areaList.values())[5]/list(areaList.values())[7],",")
                outputField.update()
            elif fromLengthDropdown.value==area5 and toLengthDropdown.value==str(list(areaList.keys())[8]):
                outputField.value=sq_hectaresTo_sq_meters=format(userinputValue*list(areaList.values())[5]/list(areaList.values())[8],",")
                outputField.update()
            elif fromLengthDropdown.value==area5 and toLengthDropdown.value==str(list(areaList.keys())[9]):
                outputField.value=sq_hectaresTo_sq_kilometers=format(userinputValue*list(areaList.values())[4]/list(areaList.values())[9],",")
                outputField.update()
                """ ...................FROM SQUARE  MILIMETERS..............."""

            elif fromLengthDropdown.value==area6 and toLengthDropdown.value==str(list(areaList.keys())[0]):
                outputField.value=sq_MilimetersTo_sq_inch=format(userinputValue*list(areaList.values())[6]/list(areaList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==area6 and toLengthDropdown.value==str(list(areaList.keys())[1]):
                outputField.value=sq_MilimetersTo_sq_feet=format(userinputValue*list(areaList.values())[6]/list(areaList.values())[1],",")
                outputField.update()
            elif fromLengthDropdown.value==area6 and toLengthDropdown.value==str(list(areaList.keys())[2]):
                outputField.value=sq_MilimetersTo_sq_Yard=format(userinputValue*list(areaList.values())[6]/list(areaList.values())[2],",")
                outputField.update()
            elif fromLengthDropdown.value==area6 and toLengthDropdown.value==str(list(areaList.keys())[4]):
                outputField.value=sq_MilimetersTo_sq_acres=format(userinputValue*list(areaList.values())[6]/list(areaList.values())[4],",")
                outputField.update()
            elif fromLengthDropdown.value==area6 and toLengthDropdown.value==str(list(areaList.keys())[5]):
                outputField.value=sq_MilimetersTo_sq_hectares=format(userinputValue*list(areaList.values())[6]/list(areaList.values())[5],",")
                outputField.update()
            elif fromLengthDropdown.value==area6 and toLengthDropdown.value==str(list(areaList.keys())[3]):
                outputField.value=sq_MilimetersTo_sq_miles=format(userinputValue*list(areaList.values())[6]/list(areaList.values())[3],",")
                outputField.update()
            elif fromLengthDropdown.value==area6 and toLengthDropdown.value==str(list(areaList.keys())[7]):
                outputField.value=sq_MilimetersTo_sq_centimeters=format(userinputValue*list(areaList.values())[6]/list(areaList.values())[7],",")
                outputField.update()
            elif fromLengthDropdown.value==area6 and toLengthDropdown.value==str(list(areaList.keys())[8]):
                outputField.value=sq_MilimetersTo_sq_meters=format(userinputValue*list(areaList.values())[6]/list(areaList.values())[8],",")
                outputField.update()
            elif fromLengthDropdown.value==area6 and toLengthDropdown.value==str(list(areaList.keys())[9]):
                outputField.value=sq_MilimetersTo_sq_kilometers=format(userinputValue*list(areaList.values())[6]/list(areaList.values())[9],",")
                outputField.update()
                """ ...................FROM SQUARE  CENTIMETERS..............."""

            elif fromLengthDropdown.value==area7 and toLengthDropdown.value==str(list(areaList.keys())[0]):
                outputField.value=sq_centimetersTo_sq_inch=format(userinputValue*list(areaList.values())[7]/list(areaList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==area7 and toLengthDropdown.value==str(list(areaList.keys())[1]):
                outputField.value=sq_centimetersTo_sq_feet=format(userinputValue*list(areaList.values())[7]/list(areaList.values())[1],",")
                outputField.update()
            elif fromLengthDropdown.value==area7 and toLengthDropdown.value==str(list(areaList.keys())[2]):
                outputField.value=sq_centimetersTo_sq_Yard=format(userinputValue*list(areaList.values())[7]/list(areaList.values())[2],",")
                outputField.update()
            elif fromLengthDropdown.value==area7 and toLengthDropdown.value==str(list(areaList.keys())[4]):
                outputField.value=sq_centimetersTo_sq_acres=format(userinputValue*list(areaList.values())[7]/list(areaList.values())[4],",")
                outputField.update()
            elif fromLengthDropdown.value==area7 and toLengthDropdown.value==str(list(areaList.keys())[5]):
                outputField.value=sq_centimetersTo_sq_hectares=format(userinputValue*list(areaList.values())[7]/list(areaList.values())[5],",")
                outputField.update()
            elif fromLengthDropdown.value==area6 and toLengthDropdown.value==str(list(areaList.keys())[6]):
                outputField.value=sq_centimetersTo_sq_milimeters=format(userinputValue*list(areaList.values())[7]/list(areaList.values())[6],",")
                outputField.update()
            elif fromLengthDropdown.value==area7 and toLengthDropdown.value==str(list(areaList.keys())[3]):
                outputField.value=sq_centimetersTo_sq_miles=format(userinputValue*list(areaList.values())[7]/list(areaList.values())[3],",")
                outputField.update()
            elif fromLengthDropdown.value==area7 and toLengthDropdown.value==str(list(areaList.keys())[8]):
                outputField.value=sq_centimetersTo_sq_meters=format(userinputValue*list(areaList.values())[7]/list(areaList.values())[8],",")
                outputField.update()
            elif fromLengthDropdown.value==area7 and toLengthDropdown.value==str(list(areaList.keys())[9]):
                outputField.value=sq_centimetersTo_sq_kilometers=format(userinputValue*list(areaList.values())[7]/list(areaList.values())[9],",")
                outputField.update()


                """ ...................FROM SQUARE  METERS..............."""

            elif fromLengthDropdown.value==area8 and toLengthDropdown.value==str(list(areaList.keys())[0]):
                outputField.value=sq_MetersTo_sq_inch=format(userinputValue*list(areaList.values())[8]/list(areaList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==area8 and toLengthDropdown.value==str(list(areaList.keys())[1]):
                outputField.value=sq_MetersTo_sq_feet=format(userinputValue*list(areaList.values())[8]/list(areaList.values())[1],",")
                outputField.update()
            elif fromLengthDropdown.value==area8 and toLengthDropdown.value==str(list(areaList.keys())[2]):
                outputField.value=sq_MetersTo_sq_Yard=format(userinputValue*list(areaList.values())[8]/list(areaList.values())[2],",")
                outputField.update()
            elif fromLengthDropdown.value==area8 and toLengthDropdown.value==str(list(areaList.keys())[4]):
                outputField.value=sq_MetersTo_sq_acres=format(userinputValue*list(areaList.values())[8]/list(areaList.values())[4],",")
                outputField.update()
            elif fromLengthDropdown.value==area8 and toLengthDropdown.value==str(list(areaList.keys())[5]):
                outputField.value=sq_MetersTo_sq_hectares=format(userinputValue*list(areaList.values())[8]/list(areaList.values())[5],",")
                outputField.update()
            elif fromLengthDropdown.value==area8 and toLengthDropdown.value==str(list(areaList.keys())[6]):
                outputField.value=sq_MetersTo_sq_milimeters=format(userinputValue*list(areaList.values())[8]/list(areaList.values())[6],",")
                outputField.update()
            elif fromLengthDropdown.value==area8 and toLengthDropdown.value==str(list(areaList.keys())[7]):
                outputField.value=sq_MetersTo_sq_centimeters=format(userinputValue*list(areaList.values())[8]/list(areaList.values())[7],",")
                outputField.update()
            elif fromLengthDropdown.value==area8 and toLengthDropdown.value==str(list(areaList.keys())[3]):
                outputField.value=sq_MetersTo_sq_meters=format(userinputValue*list(areaList.values())[8]/list(areaList.values())[3],",")
                outputField.update()
            elif fromLengthDropdown.value==area8 and toLengthDropdown.value==str(list(areaList.keys())[9]):
                outputField.value=sq_MetersTo_sq_kilometers=format(userinputValue*list(areaList.values())[8]/list(areaList.values())[9],",")
                outputField.update()

                """ ...................FROM SQUARE  KILOMETERS..............."""

            elif fromLengthDropdown.value==area9 and toLengthDropdown.value==str(list(areaList.keys())[0]):
                outputField.value=sq_KilometersTo_sq_inch=format(userinputValue*list(areaList.values())[9]/list(areaList.values())[0],",")
                outputField.update()
            elif fromLengthDropdown.value==area9 and toLengthDropdown.value==str(list(areaList.keys())[1]):
                outputField.value=sq_KilometersTo_sq_feet=format(userinputValue*list(areaList.values())[9]/list(areaList.values())[1],",")
                outputField.update()
            elif fromLengthDropdown.value==area9 and toLengthDropdown.value==str(list(areaList.keys())[2]):
                outputField.value=sq_KilomileTo_sq_Yard=format(userinputValue*list(areaList.values())[9]/list(areaList.values())[2],",")
                outputField.update()
            elif fromLengthDropdown.value==area9 and toLengthDropdown.value==str(list(areaList.keys())[4]):
                outputField.value=sq_KilometersTo_sq_acres=format(userinputValue*list(areaList.values())[9]/list(areaList.values())[4],",")
                outputField.update()
            elif fromLengthDropdown.value==area9 and toLengthDropdown.value==str(list(areaList.keys())[5]):
                outputField.value=sq_KilometersTo_sq_hectares=format(userinputValue*list(areaList.values())[9]/list(areaList.values())[5],",")
                outputField.update()
            elif fromLengthDropdown.value==area9 and toLengthDropdown.value==str(list(areaList.keys())[6]):
                outputField.value=sq_KilometersTo_sq_milimeters=format(userinputValue*list(areaList.values())[9]/list(areaList.values())[6],",")
                outputField.update()
            elif fromLengthDropdown.value==area9 and toLengthDropdown.value==str(list(areaList.keys())[7]):
                outputField.value=sq_KilometersTo_sq_centimeters=format(userinputValue*list(areaList.values())[9]/list(areaList.values())[7],",")
                outputField.update()
            elif fromLengthDropdown.value==area9 and toLengthDropdown.value==str(list(areaList.keys())[8]):
                outputField.value=sq_KilometersTo_sq_meters=format(userinputValue*list(areaList.values())[9]/list(areaList.values())[8],",")
                outputField.update()
            elif fromLengthDropdown.value==area9 and toLengthDropdown.value==str(list(areaList.keys())[3]):
                outputField.value=sq_KilometersTo_sq_miles=format(userinputValue*list(areaList.values())[9]/list(areaList.values())[3],",")
                outputField.update()

        except ValueError:
                outputField.update()

                print("null")
        page.update()
    outputField=TextField(value='1',width=100,text_align=TextAlign.CENTER,autofocus=True)
    swapvalue=1/float(outputField.value.replace(",",''))
    # print(areaList.values())






# TOGGLE BUTTONS
    """ returns the reverse conversion of the current choice"""
    swapLeft=fromLengthDropdown.value 
    value_be4_swap=outputField.value
    toggle_state=True
    def reversedConversion(e):
        nonlocal toggle_state
        toggle_state = not toggle_state
        value_be4_swap=str(outputField.value)
        outputField.value= 1/float(value_be4_swap.replace(",",'')) if toggle_state else 1/float(value_be4_swap.replace(",",''))
        
        if  toggle_state:
            fromLengthDropdown.value,toLengthDropdown.value=toLengthDropdown.value,fromLengthDropdown.value
        else:
            fromLengthDropdown.value,toLengthDropdown.value=toLengthDropdown.value,fromLengthDropdown.value

        ReverseBtn.text = "ON" if toggle_state else "OFF"
        ReverseBtn.bgcolor = ft.colors.GREEN if toggle_state else ft.colors.RED
        page.update()

    ReverseBtn= IconButton(icon=icons.SWAP_HORIZ_SHARP,height=40,width=40,bgcolor=ft.colors.GREEN,on_click=reversedConversion)
    


# CLEAR FIELDS
    def clearFields(e):
        userinput.value=''
        outputField.value=''
        userinput.update()
        outputField.update()
    clearButton=Row(
        # width=100,
        alignment=MainAxisAlignment.CENTER,
        controls=[
            TextButton("clear",on_click=clearFields,style=ButtonStyle(color='black',bgcolor=colors.CYAN_100)),
                ]
                    )
    
# THE OUTPUT FIELD
    outputField=TextField(value='1',width=200,text_align=TextAlign.CENTER,autofocus=True)
    

    """.........RUNNING FUNCTIONS ON CHANGE OF EVENTS................"""
    def combined_function(e):
        checkField(e)
        compute(e)
        page.update()
    userinput.on_change=combined_function
    fromLengthDropdown.on_change=compute
    toLengthDropdown.on_change=compute
    page.update()
    # swapvalue=1/float(outputField.value.replace(",",''))
    """..........INCREMENT OR REDUCE VALUE BY 1"""
    def addition(e):
        userinput.value=float(userinput.value)
        userinput.value+=1  
        combined_function(e) 
        userinput.update()
    def minus(e):
        userinput.value=float(userinput.value)
        userinput.value-=1  
        combined_function(e) 
        userinput.update()

  

    addition_button=IconButton(icon=icons.ADD_CIRCLE_OUTLINE_OUTLINED,on_click=addition)
    minus_button=IconButton(icon=icons.REMOVE_CIRCLE_OUTLINE,on_click=minus,padding=2)
    page.update()
# ADDITION OF CONTROLS ONTO THE PAGE
    page.add(SafeArea(
        content=Column(
            spacing=10,
            controls=[
                typeContainer,
                Container(
                    padding=padding.only(top=10,bottom=40),
                    content=(
                        Row(
                            # height=60,
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                fromLengthDropdown,ReverseBtn,toLengthDropdown,
                            ]
                        )
                    )
                ),
                Container(
                    padding=padding.only(top=0,bottom=1),
                    content=(
                        Row(
                            spacing=7,
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                minus_button,userinput,addition_button
                            ]
                        )
                    )
                ),
                Container(
                    # padding=padding.only(left=0,bottom=0),
                    # margin=margin.only(left=10),
                    content=(
                        Row(
                            alignment=MainAxisAlignment.START,
                            spacing=5,
                            controls=[
                                Text(value='Result',width=65,size=22,style=TextStyle(weight=FontWeight.BOLD)),outputField
                            ]
                        )
                    )
                ),clearButton,
                
                ft.Text(value="....A product by:\n...Karyeija Felex.....",size=32,style=TextStyle(weight=FontWeight.BOLD)),


            ]
        )
    )
),

    

    page.update()
app(target=main,assets_dir="assets")
