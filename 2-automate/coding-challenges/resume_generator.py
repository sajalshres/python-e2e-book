import os
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

class resume_generator(object):
        
    def __init__(self, db):
        self._db = db
        self._md = md()
    
    def getData(self, header):
        return self._db[header]
    
    def getHeaders(self):
        return self._db.keys()
    
    def getFileName(self):
        return '{name}-resume.md'.format(name=self._db['personal_info']['name'].split(' ')[0])
    
    def writeString(self, f, txt):
        r = f
        r += txt
        return r
    
    def prepareResume(self):
        w=''
        w = self.writeString(w,self._md.getHeader('Resume',1))            
        for k1, v1 in self._db.items():
            if(k1 == 'personal_info'):
                w = self.writeString(w,self._md.getParagraph(self.getData(k1)))
                w = self.writeString(w,'\n')
            elif(k1 == 'objective'):
                w = self.writeString(w,self._md.getHeader(k1.title(),2))
                w = self.writeString(w,v1+'\n')
                w = self.writeString(w,'\n')
            elif(k1 == 'education'):
                w = self.writeString(w,self._md.getHeader(k1.title(),2))
                for i in v1:
                    w = self.writeString(w,self._md.getHeader('{institution}, {location}, {year}'.format(institution=i['institution'].title(), location=i['location'].title(), year=str(i['year'])),4))
                    w = self.writeString(w,self._md.getList([i['degree'],i['description']],'u'))
                    w = self.writeString(w,'\n')
            elif(k1 == 'employment'):
                w = self.writeString(w,self._md.getHeader(k1.title(),2))
                for i in v1:
                    w = self.writeString(w,self._md.getHeader('{role}, {year}'.format(role=i['role'].title(),year=str(i['year'])),4))
                    w = self.writeString(w,'{company}, {location}\n'.format(company=i['company'].title(),location=i['location'].title()))
                    w = self.writeString(w, self._md.getList(i['description'],'u'))
                    w = self.writeString(w,'\n')
            else:
                w = self.writeString(w,self._md.getHeader(k1.title(),2))
                w = self.writeString(w, self._md.getList(v1,'u'))
                w = self.writeString(w,'\n')
        return w
    
    def writeFile(self, w, txt):
        w.write(txt)
        
    def create(self,option='w'):
        fileName = self.getFileName()
        resume = self.prepareResume()
        
        if ( option == 'w'):
            with open(fileName,'w') as w:
                self.writeFile(w,resume)
        else:
            print(resume)
            

import db
d = db.db()
rg = resume_generator(d._db)
rg.create()

# print(md().getParagraph(d._db["personal_info"]))