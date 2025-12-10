import pandas as pd
import dash
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(URL)
year_list = [i for i in range(1980, 2024,1)]
app = dash.Dash(__name__)
app.layout = html.Div(children=[ html.H1('Automobile Sales Statistics Dashboard', 
                                style={'textAlign': 'center', 'color': '#503D36','font-size': 24}),
                    html.Div([
                                html.Div([
                                    html.H2('Report type'), 
                                        dcc.Dropdown(id='Dropdown-Statistics', options=[{'label':'Yearly Statistics', 'value':'Yearly Statistics'},
                                                            {'label':'Recession Period Statistics', 'value':'Recession Period Statistics'}],
                                                            placeholder='select a report type', value='Select Statistics',
                                                            style={'textAlign':'center','width':'80%', 'padding': '3px', 'font-size': 20})
                                        ]),
                                html.Div([
                                    html.H2('Year'),
                                          dcc.Dropdown(id='Select-year', options=[{'label': i, 'value': i} for i in year_list],
                                                            placeholder='select year',  value='Select-year',
                                                            style={'textAlign':'center','width':'80%', 'padding': '3px', 'font-size': 20})
                                        ]),          
                                html.Div([
                                    html.Div(id='output-container', className='chart-grid', style={'display':'flex'}),
                                         ])
                            ])
])

@app.callback(
    Output(component_id='Select-year', component_property='disabled'),
    Input(component_id='Dropdown-Statistics', component_property='value')
             )
def update_input_container(select_type):
    if select_type == 'Yearly Statistics':
        return False
    else:
        return True
    
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='Dropdown-Statistics', component_property='value'),Input(component_id='Select-year', component_property='value')]
             )   

def update_output_container(input_period, input_year):
    if input_period == 'Recession Period Statistics':
        recession_data = df[df['Recession'] == 1] 
        avg_sale = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
        figure= px.line(avg_sale, x='Year',y='Automobile_Sales',title='Automobile Sales during Recession'))
        type_sale = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 =dcc.Graph(
        figure=px.bar(type_sale, x='Vehicle_Type', y='Automobile_Sales',
                      title='Average Sale for each type of Vehicle', labels={'x': 'Vehicle type', 'y': 'Avg. Sale(count)'})
        )
        car_adv = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure= px.pie(car_adv, values='Advertising_Expenditure', names='Vehicle_Type', 
                           title='Advertising Expenditure for each type of vehivle during Recession' )
        )
        unem_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unem_data, x='unemployment_rate', y='Automobile_Sales',
                      title='Effect of Unemployment Rate on Vehicle Type and Sales', 
                      labels={'x': 'Unemployment Rate', 'y': 'Avg. Sale(count)'})
        )
        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1),html.Div(children=R_chart2)],style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3),html.Div(children=R_chart4)],style={'display': 'flex'})
            ]
    elif input_period == 'Yearly Statistics' and input_year is not None:
        df_year = df[df['Year'] == input_year]
        avg_sale1 = df.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
        figure= px.line(avg_sale1, x='Year',y='Automobile_Sales',title='Automobile Sales over Time'))
        avg_sale_month = df.groupby('Month')['Automobile_Sales'].mean().reset_index()
        Y_chart2 = dcc.Graph(
        figure= px.line(avg_sale_month, x='Month',y='Automobile_Sales',title='Total Monthly Automobile Sales'))
        avg_sale_year = df.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
        figure= px.bar(avg_sale_year, x='Year',y='Automobile_Sales',
                        title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))
        car_adv_y = df_year.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
        figure= px.pie(car_adv_y, values='Advertising_Expenditure',names='Vehicle_Type',
                        title= 'Total Advertisment Expenditure for Each Vehicle'))
        return [
            html.Div(className='chart-item', children=[html.Div(children=Y_chart1),html.Div(children=Y_chart2)],style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=Y_chart3),html.Div(children=Y_chart4)],style={'display': 'flex'})
            ]
    
                                
if __name__ == '__main__':
  
    app.run()