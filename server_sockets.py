import socket


class ServerSockets:
    def __init__(self, how_much_can_connect=2):
        # self.ips = how_ip_can_connect
        self.number_players = how_much_can_connect
        self.nick_ip = []

    def connect(self):
        """
        Подключение всех игроков

        """
        sock = socket.socket()
        sock.bind(('', 9901))
        sock.listen(self.number_players)
        while len(self.nick_ip) < self.number_players:
            conn, addr = sock.accept()
            data = conn.recv(1024)
            nickname = data.decode('utf-8')
            self.nick_ip.append((conn, addr[0], nickname))

    def send_message(self, number, message):
        """
        Отправка сообщения указанному ip

        """
        self.nick_ip[number][0].send('message'.encode("utf-8"))

    def recv_message(self, ip=''):
        """
        Принять сообщение от уазанного
        или любого ip

        """
        pass
