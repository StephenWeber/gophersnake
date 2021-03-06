import yaml

ENDLINE = '.\r\n'

ENTITY_FILE = 0
ENTITY_DIR  = 1


class GopherEntity:
    def __init__(self, value, name, path, content=None, server='localhost', port='7070'):
        self.type = value
        self.name = name
        self.path = path
        if content is None:
            self.default_content()
        else:
            self.content = content
        self.server = server
        self.port = port

    def entity_value(self):
        if self.type == 'GopherDir':
            return ENTITY_DIR
        else:
            return ENTITY_FILE

    def default_content(self):
        if self.type == ENTITY_DIR:
            self.content = []
        else:
            self.content = ''

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
        print({p: e.name for p, e in self.routes.items()})

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


def load_from_file(filename):
    with open(filename) as fp:
        raw_data = fp.read()

    yaml_data = yaml.load(raw_data)
    tree = process_tree(yaml_data, [], [])
    return tree


def process_tree(data, results, context):
    for item in data:
        _t = item.get('type', 'GopherFile')
        if _t == 'GopherFile':
            del item['type']
            results.append(GopherFile(**item))
        else:
            del item['type']
            _p = item.get('path')
            if ':' not in _p:
                item['path'] = _p + ':base'
            item['content'] = process_tree(item.get('content'), [], context)
            results.append(GopherDirectory(**item))
    return results
