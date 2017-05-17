import socket


def make_socket() -> socket.socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('localhost', 7070)
    print('Connecting to {}:{}'.format(*address))
    s.bind(address)
    return s


class GopherServer:
    def __init__(self):
        self.items = ['Hello to my server\thello\tlocalhost\t7070']

    def match(self, input):
        if input == b'/\r\n' or input == b'\r\n':
            return '\r\n'.join('0{}'.format(x) for x in self.items) + '\r\n.\r\n'
        if input == b'hello\r\n':
            return 'Text for the hello file'
        else:
            return '.\r\n'


def main():
    print('Process started...')
    sock = make_socket()
    sock.listen(1)
    g = GopherServer()
    while True:
        conn, address = sock.accept()
        print('Received connection from address {}'.format(address))
        with conn:
            data = conn.recv(256)
            print('received {}'.format(data))
            response = g.match(data).encode('ascii')
            print('response {}'.format(response))
            conn.sendall(response)


if __name__ == '__main__':
    main()
