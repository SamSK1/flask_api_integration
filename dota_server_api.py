from flask import Flask, render_template, request
from waitress import serve
import webbrowser

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('main_page.html')

# @app.route('/weather')
# def get_weather():
#     city=request.args.get('city1')
#     if type(city)==None:
#         city='Zurich'
        
#     elif bool(city.strip())==False:
#         city='Zurich'
        
#     weather_data=get_current_weather(city)
#     if  weather_data['cod']!=200:
#         weather_data=get_current_weather(city)
#         return webbrowser.open_new_tab('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
#     weather_data=get_current_weather(city)
#     print('!!!!')
#     return render_template(
#         "weather.html",
#         title=weather_data['name'],
#         status=weather_data["weather"][0]["description"].capitalize(),
#         temp=f"{weather_data['main']['temp']:.1f}",
#         feels_like=f"{weather_data['main']['feels_like']:.1f}"

#     )
if __name__=="__main__":
    serve(app, port=8000)