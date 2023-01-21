import re


class HTMLParser:
    """
    Строитель для пошаговой обработки HTML документа.
    """
    single: set[str] = {'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self, html_doc: str):
        self.html = html_doc

    def add_eol(self, before_value: bool = True):
        pattern = re.compile(r'<(!-- )?/?\w+.*?( --)?>', re.S)
        bf = '\n' if before_value else ''
        return HTMLParser(pattern.sub(rf'\n\g<0>{bf}', self.html))

    def optimize_eol(self) -> 'HTMLParser':
        pattern = re.compile(r'\n{2,10}')
        return HTMLParser(pattern.sub('\n', self.html))

    def delete_eol(self) -> 'HTMLParser':
        pattern = re.compile(r'>\s*<')
        return HTMLParser(pattern.sub('><', self.html))

    def delete_empty(self) -> 'HTMLParser':
        pattern = re.compile(r'<(?P<tag>\w+?)>\s*</(?P=tag)>', re.S)
        return HTMLParser(pattern.sub('', self.html))

    def delete_tags(self, *tags: str) -> 'HTMLParser':
        """Важно: теги контейнеры удаляются вместе со всем содержимым, включая любые вложенные теги!"""
        q = self.html
        for tag in set(tags) - self.single:
            pat_op = re.compile(rf'<{tag}.*?>.*?<(?P<slash>/?){tag}', re.S)
            pat_cl = re.compile(rf'</{tag}.*?>.*?<(?P<slash>/?){tag}', re.S)
            lt = len(tag)
            while mo := pat_op.search(q):
                if mo:
                    sl = 1 if mo['slash'] else 0
                    start, i = mo.start(), mo.end() - (lt + sl + 1)
                    c = 1
                    while True:
                        if mo := pat_op.match(q, i):
                            sl = 1 if mo['slash'] else 0
                            i = mo.end() - (lt + sl + 1)
                            c += 1
                        elif mo := pat_cl.match(q, i):
                            sl = 1 if mo['slash'] else 0
                            if c > 1:
                                i = mo.end() - (lt + sl + 1)
                            elif c == 1:
                                i += lt + 3
                            c -= 1
                        else:
                            i += lt + 3
                            c -= 1
                        if not c:
                            break
                    q = q[:start] + q[i:]

        for tag in set(tags) & self.single:
            pattern = re.compile(rf'<{tag}.*?>', re.S)
            q = pattern.sub('', q)

        return HTMLParser(q)

    def delete_attrs(self, *attrs: str, all: bool = False) -> 'HTMLParser':
        q = self.html
        if all:
            pattern = re.compile(r'<\w+?( .*?)?>', re.S)
            q = pattern.sub(r'<\g<name>>', q)
        else:
            for attr_key in attrs:
                pattern = re.compile(rf'\s+?{attr_key}=\".*?\"')
                q = pattern.sub('', q)
        return HTMLParser(q)



class HTMLTag:
    """
    Описывает HTML тег (с атрибутами или без), который может содержать вложенные теги (с атрибутами или без).
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = '', **kwargs):
        self.name = name
        self.value = value
        self.__nested: list[HTMLTag] = []
        self.arguments = kwargs
        r = []
        for k, v in self.arguments.items():
            r.append(f' {k}: "{v}"')
        self.res = ', '.join(r)


    @property
    def nested(self):
        """Возвращает неиндексируемый итератор по всем вложенным тегам."""
        return iter(self.__nested)

    @nested.setter
    def nested(self, value: 'HTMLTag'):
        """Добавляет вложенный тег к текущему."""
        self.__nested += [value]

    def __str(self, indent_level: int) -> str:
        """Рекурсивно формирует строку с текущим и всеми вложенными тегами и их атрибутами."""
        margin = ' ' * indent_level * self.default_indent_spaces
        eol = ''
        result = f"{margin}<{self.name}{self.res}>{self.value}"
        if self.__nested:
            for tag in self.__nested:
                result += '\n' + tag.__str(indent_level+1)
            eol = f'\n{margin}'
        result += f"{eol}</{self.name}>"
        return result

    def __str__(self):
        return self.__str(0)

    # в данной реализации нецелесообразно "прятать" класс HTMLBuilder
    @staticmethod
    def create(name: str, value: str = '', **kwargs):
        return HTMLBuilder(name, value, **kwargs)


class HTMLBuilder:
    """
    Предоставляет методы для пошаговой инициализации экземпляра HTMLTag.
    """
    def __init__(self, root: HTMLTag | str, value: str = '', **kwargs):
        if isinstance(root, HTMLTag):
            self.root = root
        elif isinstance(root, str):
            self.root = HTMLTag(root, value, **kwargs)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')

    def nested(self, name: str, value: str = '', **kwargs) -> 'HTMLBuilder':
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега."""

        tag = HTMLTag(name, value, **kwargs)
        self.root.nested = tag
        return HTMLBuilder(tag)

    def sibling(self, name: str, value: str = '', **kwargs) -> 'HTMLBuilder':
        """Добавляет вложенный тег к текущему тегу и возвращает текущий строитель."""
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested = tag
        return self

    def build(self) -> HTMLTag:
        return self.root


class HTMLEditor:
    """Фасад для взаимодействия с HTML элементами."""
    def __init__(self, html_code: str):
        self.html_code = html_code
        self.edited_code = HTMLParser(self.html_code)

    def compress(self):
        """Удаляет все символы пространства между тегами и пустые теги."""
        return self.edited_code.delete_eol().html


    def form_indents(self):
        """Добавляет символы пространства для формирования отступов вложенных тегов."""
        processing = str(self.edited_code.delete_eol().html)
        processing2 = str(HTMLParser(processing).add_eol().html)
        lst = list(processing2.split('\n'))[1:-1]
        for i in lst:
            if i == '':
                lst.remove(i)
        root = HTMLTag.create(lst[0][1:-1])
        fragments = root

        flag = False
        for c in range(1, len(lst) - 1):
            if flag:
                flag = False
                continue
            else:
                current = lst[c]
                m = re.match(r'<\w+\s*[^>]*>', current)
                if m is not None:
                    for n in range(c + 1, len(lst) - 1):
                        next = lst[n]
                        m = re.match(r'<\w+\s*[^>]*>', next)
                        if m is not None:
                            for a in range(n + 1, len(lst) - 1):
                                after_next = lst[a]
                                fragments = root.nested(current[1:-1]).sibling(next[1:-1], after_next)
                                flag = True
                                break
                            break
                        else:
                            m = re.match(r'</*\w+\s*[^>]*>', next)
                            if m is not None:
                                break
                            else:
                                fragments.sibling(current[1:-1], next)
                                break
                    else:
                        continue
        return root.build()


txt = """<div>   <h1>Title</h1>   <p>text1</p>        <p>text2</p>  <p> <p>text3</p></p> </div>"""
txt2 = """<html><body>  <h1>Заголовок</h1>    <p>Первый абзац.</p>       <p>Второй абзац.</p></body>    </html>"""
res_ver1 = HTMLEditor(txt).compress()
res1 = HTMLEditor(txt).form_indents()
res_ver2 = HTMLEditor(txt2).compress()
res2 = HTMLEditor(txt2).form_indents()
print(res_ver1)
print('-'*30)
print(res1)
print('-'*30)
print(res_ver2)
print('-'*30)
print(res2)

# stdout:
# <div><h1>Title</h1><p>text1</p><p>text2</p><p><p>text3</p></p></div>
# ------------------------------
# <div>
#   <h1>Title</h1>
#   <p>text1</p>
#   <p>text2</p>
#   <p>
#     <p>text3</p>
#   </p>
# </div>
# ------------------------------
# <html><body><h1>Заголовок</h1><p>Первый абзац.</p><p>Второй абзац.</p></body></html>
# ------------------------------
# <html>
#   <body>
#     <h1>Заголовок</h1>
#     <p>Первый абзац.</p>
#     <p>Второй абзац.</p>
#   </body>
# </html>
