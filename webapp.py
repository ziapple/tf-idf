from flask import Flask
from flask import request
import os
import json
import service1

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
# curl -H "Content-Type: application/json" -X POST  --data "{
# \"std\":\"开辟了中国特色社会主义道路，形成了中国特色社会主义理论体系\",
# \"answer\":[\"从百姓民生到重大事件，以“以故事讲思想”的方式原汁原味的再现了历史和人民是为什么选择了中国共产党、选择了社会主义、选择了改革开放\",\"准确的解读了我们党成功的根本原因。正是我们党的正确引领，才有了新中国的诞生、发展和强大，该书从解放前到当今社会，从政治体制到经济体育\"]}"
# http://localhost:5000/parse
@app.route('/parse', methods=['POST'])
def parse():
    params = json.loads(request.get_data(as_text=True))
    std = params['std']
    # 传入数组
    answer = params['answer']
    # result = service.apply(std, answer)
    vec1, vec2 = service1.get_word_vector(std, answer)
    dist1 = service1.cos_dist(vec1, vec2)
    # arr = []
    # for t in result:
    #    arr.append(t[1])
    # return str(arr)
    return str(dist1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)