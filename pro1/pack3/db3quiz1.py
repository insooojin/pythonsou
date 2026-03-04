import MySQLdb
import pickle
"""
문1) jikwon 테이블 자료 출력

키보드로부터 부서번호를 입력받아, 해당 부서에 직원 자료 출력

 부서번호 입력 : _______

직원번호 직원명 근무지역 직급

1 홍길동 서울 이사

...

인원 수 :

"""


config = {
    'host': '192.168.0.7',
    'user' : 'root',        # 실습에서는 root 말고 새로 생성해서 해보기
    'password' : '123',
    'database' : 'test',
    'port':3306,
    'charset':'utf8'
}

with open('mydb.dat', 'wb') as f:
    pickle.dump(config, f)


with open('mydb.dat', 'rb') as f:
    config = pickle.load(f)

print(config)


def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()


        bu_no = input('부서번호 입력:')
        # print(bu_no)
        sql = """
            select jikwonno as 직원번호, jikwonname as 직원명, buserloc as 근무지역, jikwonjik as 직급 
            from jikwon
            inner join buser on busernum = buserno
            where busernum ={0}
        """.format(bu_no)
        # print(sql)

        cursor.execute(sql)
        datas = cursor.fetchall()
        # print(datas)
        if len(datas) == 0:
            print(bu_no + "번 부서는 없어요")
            return          # sys.exit(0)
        
        for jikwonno, jikwonname, buserloc, jikwonjik in datas:
            print(jikwonno, jikwonname, buserloc, jikwonjik)

        print('인원 수: ', len(datas))
        

    except Exception as e:
        print('err: ', e)

    finally:
        cursor.close()
        conn.close()
        
        
if __name__=="__main__":
    chulbal()




"""
문2-1) 직원번호와 직원명을 입력(로그인)하여 성공하면 아래의 내용 출력

해당 직원이 근무하는 부서 내의 직원 전부를 직급별 오름차순우로 출력. 직급이 같으면 이름별 오름차순한다.

직원번호 입력 : _______

직원명 입력 : _______

직원번호 직원명 부서명 부서전화 직급 성별

1 홍길동 총무부 111-1111 이사 남

...

직원 수 :

이어서 로그인한 해당 직원이 관리하는 고객 자료도 출력한다.

고객번호 고객명 고객전화 나이

1 사오정 555-5555 34

관리 고객 수 :
"""
print()
def mun2_1():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()


        jikwon_no = input('직원번호 입력:')
        jikwon_name = input('직원이름 입력:')
       
        sql = """
            select jikwonno as 직원번호, jikwonname as 직원명, busername as 부서명, 
            busertel as 부서전화, jikwonjik as 직급, jikwongen as 성별 
            from jikwon
            inner join buser on busernum = buserno
            where busernum = (select busernum from jikwon where jikwonno = %s)
        """
        # print(sql)

        cursor.execute(sql, (jikwon_no,))
        datas = cursor.fetchall()
        # print(datas)
        if len(datas) == 0:
            print(f"{jikwon_name} 직원은 없어요")
            return          # sys.exit(0)
        
        for jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen in datas:
            print(jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen)

        print('인원 수: ', len(datas))

    except Exception as e:
        print('err: ', e)

    finally:
        cursor.close()
        conn.close()
            
if __name__=="__main__":
    mun2_1()
