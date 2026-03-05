import pickle

config = {
    'host': '127.0.0.1',
    'user' : 'root',        # 실습에서는 root 말고 새로 생성해서 해보기
    'password' : '123',
    'database' : 'test',
    'port':3306,
    'charset':'utf8'
}

with open('mydb.dat', mode='wb') as obj:
    pickle.dump(config, obj)