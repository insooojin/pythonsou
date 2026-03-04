import MySQLdb
config = {
    'host': '192.168.0.7',
    'user' : 'root',        # 실습에서는 root 말고 새로 생성해서 해보기
    'password' : '123',
    'database' : 'test',
    'port':3306,
    'charset':'utf8'
}

def chulbal():
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
            where jikwonno =%s and jikwonname = %s
        """.format(jikwon_no, jikwon_name)
        # print(sql)

        cursor.execute(sql, (jikwon_no, jikwon_name))
        datas = cursor.fetchall()
        # print(datas)
        if len(datas) == 0:
            print(f"{jikwon_name} 직원은 없어요")
            return          # sys.exit(0)
        
        for jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen in datas:
            print(jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen)
        

    except Exception as e:
        print('err: ', e)

    finally:
        cursor.close()
        conn.close()
            
if __name__=="__main__":
    chulbal()