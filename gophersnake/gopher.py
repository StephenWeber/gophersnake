ENDLINE = '.\r\n'

ENTITY_FILE = 0
ENTITY_DIR  = 1


class GopherEntity:
    def __init__(self, entity_type, name, path, content, server='localhost', port='7070'):
        self.type = entity_type
        self.name = name
        self.path = path
        self.content = content
        self.server = server
        self.port = port

    def __str__(self):
        return '{e.type}{e.name}\t{e.path}\t{e.server}\t{e.port}\r\n'.format(e=self)


class GopherFile(GopherEntity):
    def __init__(self, name, path, content, server='localhost', port='7070'):
        super().__init__(ENTITY_FILE, name, path, content, server, port)


class GopherDirectory:
    def __init__(self, name, path, content, server='localhost', port='7070'):
        super().__init__(ENTITY_DIR, name, path, content, server, port)
