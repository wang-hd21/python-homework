import argparse
import random
from ast import parse
def get_parser():
    parser=argparse.ArgumentParser()
    parser.add_argument('-r','--random',action='count',help='make the wordbook random')
    parser.add_argument('-t','--translate',action='count',help='translate the word')
    parser.add_argument('-s','--start',nargs=1,type=int,default=[1],help='choose the beginning of the source wordbook')
    parser.add_argument('-l','--length',nargs=1,type=int,default=[10],help='choose how many word in you wordbook')
    parser.add_argument('-n','--number',nargs=1,type=int,default=[1],help='choose how many wordbooks will be made')
    return parser
if __name__=='__main__':
    file='src.txt'
    file1='srctrans.txt'
    fb=open(file,mode='r',encoding='utf-8')
    fb1=open(file1,mode='r',encoding='utf-8')
    words=fb.readlines()
    wordtrans=fb1.readlines()
    for a in words:
        if a=='\n':
            words.remove(a)
    for a in wordtrans:
        if a=='\n':
            wordtrans.remove(a)
    d={}
    for i in range(0,len(words)):
        d[words[i]]=wordtrans[i]
    paser=get_parser()
    args=paser.parse_args()
    wordlist=words[args.start[0]-1:min(args.length[0]+args.start[0]-1,len(words))]
    for i in range(0,args.number[0]):
        file=f"test{i+1}.txt"
        fb2=open(file,mode='w',encoding='utf-8')
        if args.random:
            random.shuffle(wordlist)
        for a in wordlist:
            fb2.write(a)
            if args.translate:
                fb2.write(d[a])
            



