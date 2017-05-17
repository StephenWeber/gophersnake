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
        super().__init__(ENTITY_FILE, name, path, [content], server, port)


class GopherDirectory(GopherEntity):
    def __init__(self, name, path, content, server='localhost', port='7070'):
        super().__init__(ENTITY_DIR, name, path, content, server, port)


class GopherRouter:
    """Take entities and handle lookup by paths."""
    def __init__(self, root, all_entities):
        self.root = root
        self.routes = self._calculate_routes(all_entities)

    def _calculate_routes(self, entities):
        routes = {}
        for e in entities:
            routes[e.path] = e
            if e.type == ENTITY_DIR:
                sub_routes = self._calculate_routes(e.content)
                routes.update(sub_routes)
        return routes

    def get_entity(self, path):
        print('Entity path requested {}'.format(path))
        if path == '/' or path == '':
            print('Returning root')
            return self.root
        return self.routes.get(path).content
