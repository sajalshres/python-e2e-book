class md(object):
    def __init__(self):
       pass

    def getHeader(self, message, level=1):
        """
        Return a markdown heading
        """
        if level in range(1,6):
            return "{0} {1}\n".format("#"*level, message)
        return None

    def getList(self, l, o = False):
        if isinstance(l,(list, set, tuple)):            
            return "\n".join([f"{i[0]+1}. {i[1]}" if o else f"* {i[1]}" for i in enumerate(l)])

md = md()
print(md.getList(["a","ab",1],False))
