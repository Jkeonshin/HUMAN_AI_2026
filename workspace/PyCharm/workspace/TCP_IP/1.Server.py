# TCP/IP 서버
# 클라이언트의 접속을 기다리며, 클라이언트가 보낸 메시지를 수신하고
# 간단한 응답을 보내는 기능

import socket
# 1. 서버 기본 설정
HOST = '192.168.133.107'    # 본인의 아이피 주소
PORT = 9998                 # 사용할 포트번호 (0~65535 중 하나 , 충돌되지 않게 잘 설정)

# 2. 소켓 객체 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. IP와 포트를 소캣에 바인딩(연결)
server_socket.bind((HOST,PORT))      # 서버가 클라이언트 요청을 받을 수 있도록 설정

# 4. 클라이언트 연결 대사 시작
server_socket.listen()               # 인자 없이 Listen() 호출 시 기본적으로 동시 접속 1개만 허용
print(f"서버가 {HOST}:{PORT}에서  연결대기중입니다...")

# 5. 클라이언트 연결 수학 (accept)
client_socket, addr = server_socket.accept()
print(f"클라이언트{addr}연결 완료")

# 6. 클라이언트와 메시지 송수신 루프
while True:
    #클라이언트로 부터 최대 1024 바이트 데이터 수신
    data = client_socket.recv(1024).decode() # 클라이언트로부터 메시지 bytes --> str 변환
    if not data:
        print("데이터 수신 종료 (클라이언트 연결 해제)")
        break
    #
    if data.lower() == "exit":
        print("데이터 수신종료 (클라이언트 연결 해제됨)")
        break

    # 수신된 메시지 출력
    print(f"클라이언트 메시지: {data}")

    #서버의 응답 생성
    reply = f"서버응답: [{data}] 잘 받았습니다."
    client_socket.sendall(reply.encode())

# 7. 연결 종료
client_socket.close()
server_socket.close()
print("서버 종료 완료")

