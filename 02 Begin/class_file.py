
class File:
  def __ini__(self):
    self.path = ''

  def printer(self, msg):
    print( msg , end='')

  def setPath(self, path):
    self.path = path
    return True

  def getPath(self):
    return self.path

  def readFile(self, name):
    f = open(self.path + name, 'r')
    content = f.read()
    f.close()
    return content

  def writeFile(self, name, content):
    return write( name, content,'w' )

  def appendFile(self, name, content):
    return write( name, content,'a' )

  def write( self, name, content, mode ):
    f = open(self.path + name, mode)
    f.write(content)
    f.close()
    return True
