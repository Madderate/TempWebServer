from tempwebserver import app
import json

name = 'madderate'
environmentList = {
    'temperature': 24,
    'humidity': 50,
    'luminous_intensity': 500,
    'air_quality': 25
}

# 处理请求
@app.route('/')
def index():
    # return render_template('index.html', environmentQuery=environmentQuery)

    # return json.dumps(environmentQuery, ensure_ascii=False)
    return json.dumps(environmentList)
