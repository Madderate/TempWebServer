from tempwebserver import app, request
import json
import random


# 处理请求
@app.route('/')
def index():
    # return render_template('index.html', environmentQuery=environmentQuery)
    # return json.dumps(environmentQuery, ensure_ascii=False)
    user = {'name': 'madderate'}
    return json.dumps(user)


@app.route('/environment')
def get_environment():
    environment = {
        'temperature': random.randint(20, 23),
        'humidity': random.randint(12, 100),
        'luminous_intensity': random.randint(200, 1600),
        'air_quality': random.randint(5, 200)
    }
    return json.dumps(environment)


@app.route('/temperature')
def get_temperature():
    temperature = {'temperature': random.randint(20, 23)}
    return json.dumps(temperature)


@app.route('/humidity')
def get_humidity():
    humidity = {'humidity': random.randint(12, 100)}
    return json.dumps(humidity)


@app.route('/luminous_intensity')
def get_luminous_intensity():
    luminousIntensity = {'luminous_intensity': random.randint(200, 1600)}
    return json.dumps(luminousIntensity)


@app.route('/air_quality')
def get_air_quality():
    airQuality = {'air_quality': random.randint(5, 200)}
    return json.dumps(airQuality)


@app.route('/switch/light', methods=['POST'])
def control_light():
    light = {}
    if request.form.get('is_lit') == 'true':
        light['is_lit'] = False
    elif request.form.get('is_lit') == 'false':
        light['is_lit'] = True
    return json.dumps(light)


@app.route('/switch/fan', methods=['POST'])
def control_fan():
    fan = {}
    if request.form.get('is_fan_on') == 'true':
        fan['is_fan_on'] = False
    elif request.form.get('is_fan_on') == 'false':
        fan['is_fan_on'] = True
    return json.dumps(fan)
