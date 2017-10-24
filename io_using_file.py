poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

f = open('poem.txt', 'w')

f.write(poem)

f.close()

f = open('poem.txt')

while True:
    line = f.readline()

    if len(line) == 0:
        break

    print(line, end='')

f.close()

# 打开模式可以是阅读模式( 'r' )，写入模式( 'w' )和追加模式( 'a' )。我们还 可以选择是通过文本模式( 't' )还是二进制模式( 'b' )来读取、写入或追加文本