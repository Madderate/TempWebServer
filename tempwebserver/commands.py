from tempwebserver import app
import json

user = {'name': 'madderate'}
environment = {
    'temperature': 24,
    'humidity': 50,
    'luminous_intensity': 500,
    'air_quality': 25
}
temperature = {'temperature': 24}
humidity = {'humidity': 50}
luminousIntensity = {'luminous_intensity': 500}
airQuality = {'air_quality': 25}


# 处理请求
@app.route('/')
def index():
    # return render_template('index.html', environmentQuery=environmentQuery)

    # return json.dumps(environmentQuery, ensure_ascii=False)
    return json.dumps(user)


@app.route('/environment')
def get_environment():
    return json.dumps(environment)


@app.route('/temperature')
def get_temperature():
    return json.dumps(temperature)


@app.route('/humidity')
def get_humidity():
    return json.dumps(humidity)


@app.route('/luminous_intensity')
def get_luminous_intensity():
    return json.dumps(luminousIntensity)


@app.route('/air_quality')
def get_air_quality():
    return json.dumps(airQuality)
