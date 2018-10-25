
from aip import AipOcr
APP_ID = '10379743'
API_KEY = 'QGGvDG2yYiVFvujo6rlX4SvD'
SECRET_KEY = 'PcEAUvFO0z0TyiCdhwrbG97iVBdyb3Pk'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('./input/1_2.jpg')

client.general(image);


options = {}
options["recognize_granularity"] = "big"
options["probability"] = "true"
##options["accuracy"] = "normal"
options["detect_direction"] = "true"


result=client.receipt(image, options)

print(len(result["words_result"]))
for i in range(len(result["words_result"])):
    print((result["words_result"][i]["words"]))

"""

# 定义常量
APP_ID = '10379743'
API_KEY = 'QGGvDG2yYiVFvujo6rlX4SvD'
SECRET_KEY = 'PcEAUvFO0z0TyiCdhwrbG97iVBdyb3Pk'

# 初始化文字识别分类器
aipOcr=AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "test1.7.JPG"

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

# 网络图片文字文字识别接口
result = aipOcr.webImage(get_file_content(filePath),options)

# 如果图片是url 调用示例如下
# result = apiOcr.webImage('http://www.xxxxxx.com/img.jpg')

print(result)
"""
"""
import sys

def return_result(w):
    return 0

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        ans.append(return_result(values))
    print(ans)
"""















"""
def return_handled_list(input_list):
    k=len(input_list)-1
    for i in range(len(input_list)-1):
        if(input_list[i]<input_list[i+1]):
            k=i
            break
    del input_list[i]
    return input_list

for j in range(num):
    input_list=return_handled_list(input_list)
ctemp=""
for i in range(len(input_list)):
    ctemp=ctemp+str(input_list[i])
print(int(ctemp))

w=[]

for i in range(1,1000):
    if i<10:
        w.append(i)
    else:
        w.append(i/10**(len(str(i))-1))

w.sort()
wtemp=[]
for i in range(len(w)):
    str_temp=""
    for c in str(w[i]):
        if c==".":
            continue
        str_temp+=c
    wtemp.append(str_temp)
print(wtemp)
"""

