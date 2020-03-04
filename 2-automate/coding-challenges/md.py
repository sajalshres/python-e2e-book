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

    def getParagraph(self, message):
        p =""
        if isinstance(message,dict):
            p = "\n".join([f"{i}" for i in message.values()])
        elif isinstance(message,(list, tuple, set)):
            p = "\n".join([f"{i}" for i in message])
        else:
            p = f"{message}\n\n"
        return p+"\n"
