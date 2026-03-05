# socket  소켓은 프로세스가 네트워크 세계로 데이터를 내보내거나 혹은 그 세계로부터 데이터를 받기 위한 실제적인 창구 역할을 한다.
# 그러므로 프로세스가 데이터를 보내거나 받기 위해서는 받드시 소켓을 열어서 소켓에 데이터를
# 소켓으로부터 데이터를 읽어들여야 한다.
# SOCKET이란 TCP/IP 의 프로그래머 인터페이스이다.
# 통신 시시간 대화가 가능하도록 하는 통신방식으로 클라이언트/서버 모델에 기초한다

# 연결지향:TCP/IP
# 비연결지향:UDP

# socket 통신 확인 port 번호 반환
import socket       #socket 모듈 필요

print(socket.getservbyname('http','tcp'))       # www 환경 전송규야
print(socket.getservbyname('ssh','tcp'))        # 원격 컴 접속 파일 전송 메일 송수신 이메일
print(socket.getservbyname('ftp','tcp'))        #파일 전송   
print(socket.getservbyname('smtp','tcp'))       #메일 송수신
print(socket.getservbyname('pop3','tcp'))       #이메일  
print()
print(socket.getaddrinfo('www.daum.net', 80, proto=socket.SOL_TCP))     # ip address 반환
print(socket.getaddrinfo('www.naver.net', 80, proto=socket.SOL_TCP))