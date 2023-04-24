

if __name__ == '__main__':
    try:
        with open('sample.txt', 'r') as file:
            data = file.read().replace('\n', '')
        l=len(data)
        nn=len(data)//600
        chunks, chunk_size = len(data), len(data)//(nn+1)
        p=[ data[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
        
        for i in range(0,len(p)):
            worddd(p[i])
            writee('\n')
            BG.save('%doutt.png'%i)
            BG1= Image.open("myfont/bg.png")
            BG=BG1
            gap = 0
            _ =0
    except ValueError as E:
        print("{}\nTry again".format(E))


