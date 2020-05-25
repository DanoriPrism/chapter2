from flask import Flask
from datetime import datetime, date, time, timedelta
from flask import jsonify 

app = Flask(__name__)

#,"Mes:",tim.month,"Día:"tim.day,"Hora:",tim.hour,"Minutos:",tim.minute,"Segundos:",tim.second

@app.route('/')
def hello_world_json_list():
    tim=datetime.now()
    data=["Año:",tim.year,"Mes:",tim.month,"Día:",tim.day,"Hora:",tim.hour,"Minutos:",tim.minute,"Segundos:",tim.second]
    
    
    return jsonify(data)
    
if __name__ == '__main__':
    app.run()
