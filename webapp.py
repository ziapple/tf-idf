from flask import Flask
from flask import request
import os
import service

app = Flask(__name__)


# 执行成功
def ok():
    return '{"code": "ok"}'


# 执行失败
def fail(msg):
    return '{"code": "500:, "msg": msg}'


# 检查端口是否存在，直接kill掉
def check_server():
    os.system("netstat -nltp|grep 5001|awk '{print $7}'|awk -F/ '{print $1}'|xargs kill -9")


# 给主观题打分
# request.json 只能够接受方法为POST、Body为raw，header 内容为 application/json类型的数据
@app.route('/parse', methods=['POST'])
def upload_file():
    params = request.json if request.method == "POST" else request.args
    std = params['std']
    answer = params['answer']
    return service.apply(std, answer)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
