import random
import json

SECRET_KEY='3d0C1LuoB_jxc"X('
AES_IV='piuhjboilhjvgbvx'

def generateTask():
    fi=open('cache/'+str(random.randint(0,99))+'.task')
    return json.loads(fi.readline()),int(fi.readline()),int(fi.readline())

def generateCoin():
    return 'INSA{W3ll_NEx7_Tim3_i_ll_sT1ck_to_hash_CracKing}'
        
if __name__=='__main__':
    for i in range(100):
        fo=open('cache/'+str(i)+'.task','w')
        a,b,c=generateTask()
        fo.write('%s\n%s\n%s\n'%(a,b,c))
        fo.close()
        print i,
