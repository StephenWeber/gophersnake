import socket

from gophersnake.gopher import GopherFile, GopherDirectory, GopherRouter


def make_socket() -> socket.socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # reuse addresses in "wait" status
    address = ('localhost', 7070)
    print('Connecting to {}:{}'.format(*address))
    s.bind(address)
    return s


class GopherServer:
    def __init__(self):
        self.items = [
            GopherFile('Hello to my server', 'hello', 'Text for the hello file'),
            GopherDirectory('Directory of Files', 'Subdir:Base', [
                GopherFile('Subfile A', 'Subdir:A', 'All Alligators Appreciate Apples'),
                GopherFile('Subfile B', 'Subdir:B', 'Buffalo Buffalo Buffalo Buffalo'),
                GopherDirectory('Subdir C', 'C Deck:base', [
                    GopherFile('Master of None', 'C Deck:mon', 'Allora...')
                ])
            ])
        ]
        self.router = GopherRouter(self.items, self.items)

    def match(self, input):
        decoded = input.decode()
        bare = decoded.strip('\r\n')
        entity = self.router.get_entity(bare)
        if entity is not None:
            return '\r\n'.join(str(e) for e in entity) + '\r\n'
        else:
            return 'Path not found.\r\n'


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
