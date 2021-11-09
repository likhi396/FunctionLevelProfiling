import os;
import re;

directory1 = os.listdir(r"C:/Users/srilikhi/likhitha/Final/ccc/")
directory2='C:/Users/srilikhi/likhitha/Final/outcc/'

il='.*inline.*\(.*|^AAEU_PROCESS.*'
sp='^\/.*\/$'
pattern1 = '^(?!\s*$|\s|\#|\*|\{|\}|\/).*\(.*$'
pattern2 = '^(?!\#|\*|\{|\}|\/).*\).*$' 
pattern3='.*\;$'
pattern4='^\{'
pattern5='^\s*return.*\;$|^\s*return\;$|^\s*return\s\.*$|^\s*return\s.*'
pattern6='^\}|^\}\s\/.*\/$|^\}\/.*\/$'
pattern7='.*\);$'
pattern8='\n'
pattern9='.*\/$'
p10='.*PRIVATE FUNCTION.*'
p11='\s.*if.*\(|.*else.*'
p12='\)$'
p13='.*\{$'
p14='.*\{$'


flag=0
flag1=0
flagp=0
flag3=0
flag5=0

store2=''
store1=''

def fun():
    for i in directory1:
        if i.endswith(".c"):
        
            with open(i) as f:
                #d=i[0]
                t=i.replace(".c",".txt")
                fp=directory2+t
                myfile=open(fp,'w')
                
                myfile.write('typedef enum {\n')
                
                
                for line in f:
                    rli=re.match(il,line)
                   
                    result1=re.match(pattern1,line)
                    result2=re.match(pattern2,line)
                    result3=re.match(pattern3,line)
                    r7=re.match(pattern7,line)
                    
                    if(rli):
                          pass
              
                    elif (result1 and not result3):
                        
                   
                   
                        
                        
                        
                        if not result2:
                         
                            global flagp
                            flagp=1
                            global store1
                            k=line.split('(')[0]
                            lk=k.split()[-1]
                            if(re.search(r'^\*.*', lk)):
                                lk=lk[1:]
                            store1=lk.upper()
                            
                            while not (result2):
                                
                                #myfile.write(line)
                                
                                line=f.readline()
                                
                                result2 = re.match(pattern2, line)
                            r7=re.match(pattern7,line)
                            if(r7):
                                flagp=0
                        
                       # myfile.write(line)
                        global store2
                        p=line.split('(')[0]
                        lp=p.split()[-1]
                        if(re.search(r'^\*.*', lp)):
                            lp=lp[1:]
                        store2=lp.upper()
                        
                        
                        line=f.readline()
                        #myfile.write(line)
                        rs=re.match(sp,line)
                        r8=re.match(pattern8,line)
                        if(r8):
                            #pass
                            line=f.readline()
                            #myfile.write(line)
                        if(rs):
                            line=f.readline()
                            #myfile.write(line)
                            #line=f.readline()
                            #myfile.write(line)
                        res4=re.match(pattern4,line)
                        global flag
                        global flag1
                        flag1=0
                        
                        if(res4):
                        
                            if (flagp and store1==lk):
                                myfile.write(store1+'FN,\n')
                            elif(flagp and store1!=lk):
                                myfile.write(store1+',\n')
                                flagp=0
                            elif not flagp:
                                if(store2==lp):
                                    myfile.write(store2+'FN,\n')
                                else:
                                    myfile.write(store2+',\n')
                                
                            #myfile.write(line)
                            #myfile.write(line+'\nStart\n')
                            #myfile.write('\tTAaSysTime64 currentTick = AaTicks64Get();\n')
                    
                myfile.write('MAX_FUN_NAME\n}eFunName;\n')
                myfile.write('\ntypedef struct profiling\n{\n u32 count;\n u32 timeTaken;\n}tProfiling;\n')
                myfile.write('\nstatic tProfiling arrProfile[MAX_FUN_NAME];\n\n')
                myfile.close()
                
def fun1():
    for i in directory1:
        if i.endswith(".c"):
            print("InputFile is:"+i)
        
            with open(i) as f:
                
                d=i
                fp=directory2+d
                myfile=open(fp,'w')
                y=1
                global flags
                flags=0
                flagk=0 
                for line in f:
                    rli=re.match(il,line)
                    result1=re.match(pattern1,line)
                    result2=re.match(pattern2,line)
                    result3=re.match(pattern3,line)
                    result4=re.match(pattern4,line)
                    result5=re.match(pattern5,line)
                    result6=re.match(pattern6,line)
                    result9=re.match(pattern9,line)
                    r10=re.match(p10,line) 
                    
                    
                    if(result9 and not flagk):
                        flagk=1
                        myfile.write(line)
                        myfile.write('/*lint -e539 */\n/*lint -e525*/\n#include <IfAaSysTime.h>\n')
                       
                
                    elif(rli):
                            myfile.write(line)
                            while not (result6):
                                
                                line=f.readline()
                                myfile.write(line)
                                result6=re.match(pattern6,line)
                    
            
                    
                    elif(r10):
                    
                     
                        myfile.write(line)
                        if(y):
                            y=0
                        
                            t=i.replace(".c",".txt")
                            fpp=directory2+t
                            myfile1=open(fpp,'r')
                            for line1 in myfile1:
                                myfile.write(line1)
                                
                    
                    elif (result1 and not result3):
                        
                        if(y):
                            y=0
                        
                            t=i.replace(".c",".txt")
                            fpp=directory2+t
                            myfile1=open(fpp,'r')
                            for line1 in myfile1:
                                myfile.write(line1)
                        
                        if not result2:
                         
                            global flagp
                            flagp=1
                            global store1
                            k=line.split('(')[0]
                            lk=k.split()[-1]
                            if(re.search(r'^\*.*', lk)):
                                lk=lk[1:]
                            
                            store1=lk.upper()
                            
                            
                            while not (result2):
                                
                                myfile.write(line)
                                
                                line=f.readline()
                            
                                result2 = re.match(pattern2, line)
                            result7=re.match(pattern7,line)
                            if(result7):
                                flagp=0
                        
                        myfile.write(line)
                        global store2
                        p=line.split('(')[0]
                        lp=p.split()[-1]
                        if(re.search(r'^\*.*', lp)):
                            lp=lp[1:]
                        store2=lp.upper()
                        
                        
                        line=f.readline()
                        #myfile.write(line)
                        rs=re.match(sp,line)
                        result8=re.match(pattern8,line)
                        while(result8):
                            #pass
                            myfile.write(line)
                            line=f.readline()
                            result8=re.match(pattern8,line)
                            
                        while(rs):
                            myfile.write(line)
                            line=f.readline()
                            rs=re.match(sp,line)
                        
                        result4=re.match(pattern4,line)
                        global flag
                        global flag1
                        flag=0
                        flag1=0
                    
                        
                        if(result4):
    
                            
                            flag=1
                            flag1=1
                            global flag3
                            
                            if flag3==0:
                               flag3=1 
                               
                            myfile.write(line)
                            #myfile.write(line+'\nStart\n')
                            myfile.write('\tTAaSysTime64 currentTick = AaTicks64Get();\n')
                        
                        else:
                           myfile.write(line)
                       
                                    
                    elif(result6 and flag):
                        p="\t\tarrProfile["
                        r="].timeTaken += AaTicks64Get() - currentTick;"
                        s="].count++;"
                        
                        
                        if(flag1 and flagp):
                            if(store1==lk):
                                myfile.write(p+store1+'FN'+r+'\n')
                                myfile.write(p+store1+'FN'+s+'\n')
                                
                                myfile.write(p+store1+'FN].count'+'='+p+store1+'FN].count;'+'\n')
                                myfile.write(line+'\n')
                                flagp=0
                            else:     
                                myfile.write(p+store1+r+'\n')
                                myfile.write(p+store1+s+'\n')
                              
                                myfile.write(p+store1+'].count'+'='+p+store1+'].count;'+'\n')
                                myfile.write(line+'\n')
                                flagp=0
                        elif(flag1 and flagp==0):
                            if(store2==lp):
                                myfile.write(p+store2+'FN'+r+'\n')
                                myfile.write(p+store2+'FN'+s+'\n')
                                
                                myfile.write(p+store2+'FN].count'+'='+p+store2+'FN].count;'+'\n')
                                myfile.write(line+'\n')
                            else:
                                myfile.write(p+store2+r+'\n')
                                myfile.write(p+store2+s+'\n')
                                
                                myfile.write(p+store2+'].count'+'='+p+store2+'].count;'+'\n')
                                myfile.write(line+'\n')
                            
                        else:
                            myfile.write(line)
                            flagp=0
                        
                        flag=0
                        
                    
                    elif(result5 and flag):
                        flag1=0
                        p="\t\t\t\tarrProfile["
                        r="].timeTaken += AaTicks64Get() - currentTick;"
                        s="].count++;"
                        if(flagp==1 and store1==lk):
                                myfile.write(p+store1+'FN'+r+'\n')
                                myfile.write(p+store1+'FN'+s+'\n')
                               
                                myfile.write(p+store1+'FN].count'+'='+p+store1+'FN].count;'+'\n')
                                myfile.write(line+'\n')
                                
                        elif(flagp==1 and store2!=lk):
                                myfile.write(p+store1+r+'\n')
                                myfile.write(p+store1+s+'\n')
                                
                                myfile.write(p+store1+'].count'+'='+p+store1+'].count;'+'\n')
                                myfile.write(line+'\n')
                                
                        elif(flagp==0):
                            if(store2==lp):
                                myfile.write(p+store2+'FN'+r+'\n')
                                myfile.write(p+store2+'FN'+s+'\n')
                              
                                myfile.write(p+store2+'FN].count'+'='+p+store2+'FN].count;'+'\n')
                                myfile.write(line+'\n')
                            
                            else:    
                                myfile.write(p+store2+r+'\n')
                                myfile.write(p+store2+s+'\n')
                                
                                myfile.write(p+store2+'].count'+'='+p+store2+'].count;'+'\n')
                                myfile.write(line+'\n')
                       
                    
                    else:
                        myfile.write(line)
                        
                    
                print(d+"\tFile created...Check the Output_Files folder!\n") 
                
            myfile.close()

fun()
fun1()
                        
                