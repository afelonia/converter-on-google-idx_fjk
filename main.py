from typing import Any,Dict
import flet as ft
import math


# from typing import Any, Dict
# nonlocal txtFields = [x1_input, y1_input, x2_input, y2_input, x3_input, y3_input, xP_input, yP_input]


def textfields() -> dict[Any]:

    return {
        # "cursor_height": 26,
        # "margin":ft.margin.only(bottom=2),
        "content_padding":ft.padding.all(10),
        # "dense":True,
        "width": 76,
        "filled": False,
        "keyboard_type": "NUMBER",  # Assuming you're passing the string identifier
        "text_size": 20,
        "autofocus": True,
        "text_align": 'left',
        "color":  "#000000",
        "col": {"xs": 6}, 
    }

# Original coordinates
a_original = (1000, 5300)
b_original = (3100, 5000)
c_original = (2200, 6300)
p_original = (2128.39044, 5578.14432)  # Coordinate to center


# Determine min/max for the chart
maxx = max(a_original[0], b_original[0], c_original[0])
maxy = max(a_original[1], b_original[1], c_original[1])
minx = min(a_original[0], b_original[0], c_original[0])
miny = min(a_original[1], b_original[1], c_original[1])


pointA=(a_original[0], a_original[1])
pointB=(b_original[0], b_original[1])
pointC=(c_original[0], c_original[1])
pointP=(p_original[0], p_original[1])


# Original coordinates
a_new = (9212.601, 454619.842)   #zz: (40575.622, 454126.524)
b_new = (38612.341, 455817.573)
c_new = (40575.622, 454126.524)
p_new = (39498.805, 458755.828) 

a_nw = (24, 12)   #zz: (40575.622, 454126.524)
b_nw = (34, 32)
c_nw = (49, 36)
p_nw = (64, 5) 


PP1=(a_new[0], a_new[1])
PP2=(b_new[0], b_new[1])
PP3=(c_new[0], c_new[1])
PP4=(p_new[0], p_new[1])

ppt=PP1,PP2,PP3,PP4

ab_new=math.dist([*a_new],[*b_new])
bc_new=math.dist([*b_new],[*c_new])
cp_new=math.dist([*c_new],[*p_new])
pa_new=math.dist([*p_new],[*a_new])



a_original = (1000, 5300)
b_original = (3100, 5000)
c_original = (2200, 6300)
p_original = (2128.39044, 5578.14432)  # Coordinate to center

ab_original=math.dist([*a_original],[*b_original])
bc_original=math.dist([*b_original],[*c_original])
cp_original=math.dist([*c_original],[*p_original])
pa_original=math.dist([*p_original],[*a_original])

    



Points=(pointA, pointB, pointC, pointP)
PTS=(a_new,b_new,c_new,p_new)
PTSS=(a_nw,b_nw,c_nw,p_nw)

def main(page: ft.Page):
    page.vertical_alignment=ft.CrossAxisAlignment.CENTER
    contHeight=page.height/2.2   
    page.adaptive = True
    page.window_bgcolor = "blue"
    page.bgcolor = ft.colors.BLACK
    page.title = "Resection"
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll='adaptive'

# # peacepark
#     MASTS	NORTHINGS(m)	EASTINGS(m)
#     Kololo(71Y41)	37212.601	454619.842
#     Naguru(71Z93)	38612.341	455817.573
#     Bahai(71Y42)	40575.622	454126.524
#     Kyambogo(71Y151)	39475.730	458776.858

# COORDINATES OF POINT X		
# EASTING(m)	458755.828	458755.828
# NORTHING(m)	39498.805	39498.805



    # print(f"ab= {ab_original}")
    # print(f"bc= {bc_original}")
    # print(f"cp= {cp_original}")
    # print(f"pa= {pa_original}")
    # Calculate the offset to center point p_scaled


    # x1_input = ft.TextField(label="X\u2081 ".upper(), col={"xs": 6})
    x1_input = ft.TextField(label="X\u2081 ".upper(),**textfields())
    y1_input = ft.TextField(label="Y\u2081".upper(), **textfields())
    x2_input = ft.TextField(label="X\u2082".upper(), **textfields())
    y2_input = ft.TextField(label="Y\u2082".upper(), **textfields())
    x3_input = ft.TextField(label="X\u2083".upper(), **textfields())
    y3_input = ft.TextField(label="Y\u2083".upper(), **textfields())
    xP_input = ft.TextField(label="x\u209a".upper(), **textfields())
    yP_input = ft.TextField(label="y\u209a".upper(), **textfields())

    
    user_location_text = ft.Text("Your Location", text_align='center', weight='bold', color="purple")
    result_text = ft.Text()

    control_section = ft.Container(
        border_radius=ft.BorderRadius(bottom_left=20,bottom_right=20,top_left=0,top_right=0),
        height=page.height*0.37,
        width=page.width,
        padding=10,
        bgcolor=ft.colors.TEAL,
        # margin=ft.margin.only(left=20,right=20),
        content=ft.ResponsiveRow(
            [
                x1_input, y1_input, x2_input, y2_input, x3_input, y3_input, user_location_text,xP_input, yP_input,
            ]
        ),
    )
    def clear_all_textfields(container):
        x1_input.value=("");y1_input.value=("")
        x2_input.value=("");y2_input.value=("")
        x3_input.value=("");y3_input.value=("")
        xP_input.value=("");yP_input.value=("")
                
    # Refresh the control to update the UI
        page.update()

    
    clear_button = ft.ElevatedButton(text="Clear All", on_click=lambda _: clear_all_textfields(page),disabled=False,bgcolor=ft.colors.PINK_100)
    page.update()

    # pointA,pointB,pointC,pointP

    # define function to draw lineChart given parameter
    def circumcenter(pts):
        x1, y1 = pts[0][0],pts[0][1]
        x2, y2 = pts[1][0],pts[1][1]
        x3, y3 = pts[2][0],pts[2][1]

        # Midpoints
        Dx = (x1 + x2) / 2
        Dy = (y1 + y2) / 2
        Ex = (x2 + x3) / 2
        Ey = (y2 + y3) / 2

        # Slopes
        if x2 != x1:
            mD = -(x2 - x1) / (y2 - y1)
        else:
            mD = float('inf')  # Vertical line case
        
        if x3 != x2:
            mE = -(x3 - x2) / (y3 - y2)
        else:
            mE = float('inf')  # Vertical line case

        # Circumcenter calculation
        if mD != float('inf'):
            bD = Dy - mD * Dx
        if mE != float('inf'):
            bE = Ey - mE * Ex

        if mD == float('inf'):
            Xc = Dx
            Yc = mE * Xc + bE
        elif mE == float('inf'):
            Xc = Ex
            Yc = mD * Xc + bD
        else:
            Xc = (bE - bD) / (mD - mE)
            Yc = mD * Xc + bD

        return Xc, Yc
        # return Xc, Yc
    def chartPoints() -> dict[Any]:
        return {
            "selected": False,  # Assuming you're passing the string identifier
            # "point":ft.ChartCirclePoint(radius=6,),
            "show_tooltip":True,
            "selected_below_line":False,
        }


    def draw_chart(pts):
        # global scale_factor_x,scale_factor_y,maxi_x,mini_x,maxi_y,mini_y,zz,radius

    
        # pts=pts
        circle_points = []
        center=circumcenter(pts[0:3])
        radius=math.dist([*center],[*pts[:3][2]])

    # def generate_circle_points(center, radius, num_points=360):
        # points = []
        num_points=360
        for i in range(num_points):
            theta = 2 * math.pi * i / num_points
            x = center[0] + radius * math.cos(theta)
            y = center[1] + radius * math.sin(theta)
            circle_points.append(ft.LineChartDataPoint(x, y,show_tooltip=False,selected_below_line=False,selected_point=False))

        eastValues=[]
        northValues=[]
        for point in pts:
            eastValues.append(point[0])
            northValues.append(point[1])

        xc_values= [point.x for point in circle_points]
        yc_values=[point.y for point in circle_points]

        x_values=eastValues
        y_values=northValues

        mini_x = min(x_values+xc_values)
        maxi_x = max(x_values+xc_values)
        mini_y = min(y_values+yc_values)
        maxi_y = max(y_values+yc_values)


        data = [
            ft.LineChartData(
                data_points=circle_points[0:],
                    stroke_width=2,
                    color=ft.colors.WHITE,
                    curved=False,
                    stroke_cap_round=True,

            ),
        ]
        data+= ft.LineChartData(
                # point=ft.ChartCirclePoint(color=ft.colors.RED,radius=6),
                # below_line_cutoff_y=5,
                data_points=[
                    ft.LineChartDataPoint(*pts[3],tooltip="P",point=ft.ChartCirclePoint(color="white"),**chartPoints()),
                    ft.LineChartDataPoint(*pts[0],tooltip="A",point=ft.ChartCirclePoint(color="pink"),**chartPoints()),
                    ft.LineChartDataPoint(*pts[1],tooltip="B",point=ft.ChartCirclePoint(color="yellow"),**chartPoints()),
                    ft.LineChartDataPoint(*pts[2],tooltip="C",point=ft.ChartCirclePoint(color="cyan"),**chartPoints()),
                    ft.LineChartDataPoint(*pts[3],tooltip="P",point=ft.ChartCirclePoint(color="white"),**chartPoints()),
                    ft.LineChartDataPoint(*pts[1],tooltip="B",point=ft.ChartCirclePoint(color="yellow"),**chartPoints()),
                    
                    
                ],
                stroke_width=2,
                color=ft.colors.WHITE,
                curved=False,
                stroke_cap_round=False,
            ),
        
        
        

        chart = ft.LineChart(
        data_series=data,
        border=ft.Border(
            bottom=ft.BorderSide(1, ft.colors.with_opacity(1, ft.colors.WHITE)),
            left=ft.BorderSide(1, ft.colors.with_opacity(1, ft.colors.WHITE)),
            top=ft.BorderSide(1, ft.colors.with_opacity(1, ft.colors.WHITE)),
            right=ft.BorderSide(1, ft.colors.with_opacity(1, ft.colors.WHITE)),
        ),
        left_axis=ft.ChartAxis(
            title=ft.Text("NORTHING", size=14,rotate=0, weight=ft.FontWeight.BOLD,style=ft.TextStyle(size=40,color="white")),
            labels=[
                # show_labels=true,

            ],
            labels_size=40,
            labels_interval=(maxi_y-mini_y)/100,
        ),
        bottom_axis=ft.ChartAxis(
            title=ft.Text("EASTING", size=14,rotate=0, weight=ft.FontWeight.BOLD,style=ft.TextStyle(size=40,color="white")),
            labels=[

            ],
            labels_size=40,
        ),
        
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=mini_y-radius,
        max_y=maxi_y+radius,
        min_x=mini_x-radius,
        max_x=maxi_x+radius,
        # animate=5000,
        expand=True,
        height=contHeight-10
    )

        return chart
    
    
    chart=draw_chart(PTSS)

    def lgnd_icons()->dict[any,str]:
        return{
            "icon":ft.icons.CIRCLE,
            "icon_size":20,
            "selected":False
        }
    legend=ft.Container(padding=ft.padding.only(left=20),
        content=ft.Row(controls=[ft.IconButton(**lgnd_icons(),icon_color="pink"),ft.Text(value="A",color="white"),ft.IconButton(**lgnd_icons(),icon_color="yellow",),ft.Text(value="B",color="white"),ft.IconButton(**lgnd_icons(),icon_color="cyan"),ft.Text(value="C",color="white"),ft.IconButton(**lgnd_icons(),icon_color="white"),ft.Text(value="P",color="white")])
    )
    # print(page.width/5.55)
    # print(page.height/3)
    content_file = ft.Container(
        margin=ft.margin.only(bottom=0),
        padding=20,
        width=page.width,
        height=page.height*0.3,
        content=chart
 
    )

    
    def on_submit(e):
        content_file.clean()
        page.update()
        try:
            x1 = float(x1_input.value)
            y1 = float(y1_input.value)
            x2 = float(x2_input.value)
            y2 = float(y2_input.value)
            x3 = float(x3_input.value)
            y3 = float(y3_input.value)
            xp = float(xP_input.value)
            yp = float(yP_input.value)
            p1,p2,p3,p4=(x1,y1),(x2,y2),(x3,y3),(xp,yp)
            newPoints= (p1,p2,p3,p4)
            chart=draw_chart(newPoints)
            content_file.content=(chart)
            page.update()

        except ValueError:
            result_text.value = "Please enter valid numbers"
            page.update()
            return

    # new_chart=draw_chart(PTS)

    page.appbar=ft.AppBar(
        title=ft.Text("Resection"),
        center_title=True,
        # elevation_on_scroll=20,
        # width=200,
        
    )

    submit_button = ft.ElevatedButton(text="Submit", on_click=on_submit, disabled=False)

    button_section = ft.Container(
        content=ft.Row(
            [submit_button,clear_button],
              alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    text=ft.Text(value="Points",color="white")
    chartTitle=ft.Text(value="Visual",color="white")
    textcont = ft.Container(
        content=ft.Row(
            [text],
              alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    chartTitlecont = ft.Container(
        content=ft.Row(
            [chartTitle],
              alignment=ft.MainAxisAlignment.CENTER,
        )
    )




    div=ft.Divider(height=18,thickness=2,color="red")


    page.add(
        ft.SafeArea(
            content=ft.Column(
                spacing=0.1,
                controls=[
                    chartTitlecont,content_file,div,textcont,legend,div,control_section,button_section
                ]
            )
        )
    )


    txtFields= [x1_input, y1_input, x2_input, y2_input, x3_input, y3_input, xP_input, yP_input]
    def check_textfields(e):
        all_valid = True
        for text_field in txtFields:
            try:
                float(text_field.value)
                text_field.color = "black"  # Set to default color if valid
                # print(text_field.value)
            except ValueError:
                text_field.color = "red"
                all_valid = False

        if all_valid and all([x1_input.value, x2_input.value, x3_input.value, xP_input.value, y1_input.value, y2_input.value, y3_input.value, yP_input.value]):
            submit_button.disabled = False
        else:
            submit_button.disabled = True
        page.update()
    for txt in txtFields:
        txt.on_change=check_textfields

    page.update()

if __name__ == "__main__":
    ft.app(target=main,assets_dir="assets")
