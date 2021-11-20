import os;
import re;

directory1 = os.listdir(r"C:/Users/srilikhi/likhitha/Final/bbb/")

directory2='C:/Users/srilikhi/likhitha/Final/outbb/'
#To Overwrite a folder
if not os.path.exists(directory2):
    os.mkdir(directory2)


inlineId='.*inline.*\(.*|^AAEU_PROCESS.*'
commentId='^\/.*\/$'
funId1 = '^(?!\s*$|\s|\#|\*|\{|\}|\/).*\(.*$'
funId2 = '^(?!\#|\*|\{|\}|\/).*\).*$' 
endwithsemicolon='.*\;$'
foundfun='^\{'
returnId='^\s*return.*\;$|^\s*return\;$|^\s*return\s\.*$|^\s*return\s.*'
spaceId='^\}|^\}\s\/.*\/$|^\}\/.*\/$'
endwithsemiId='.*\);$'
newlineId='\n'
endComment='.*\/$'
pvtFuncId='.*PRIVATE FUNCTION.*'

flagEnd=0
flagReturn=0
flagFun=0
flagStartTick=0


storeFName=''
storeFname=''

#Creates Text cfile to include enum and struct profiling typedefs 
def textFile():
    for cfile in directory1:
        if cfile.endswith(".c"):
        
            with open(cfile) as file:
                #Creating a text file with the same name as c cfile 
                t=cfile.replace(".c",".txt")
                path=directory2+t
                myfile=open(path,'w')
                
                myfile.write('typedef enum {\n')
                
                for line in file:
                    resInline=re.match(inlineId,line)
                   
                    resFunId1=re.match(funId1,line)
                    resFunId2=re.match(funId2,line)
                    resEndwithSem=re.match(endwithsemicolon,line)
                    resEndwithSemId=re.match(endwithsemiId,line)
                    
                    if(resInline):
                          pass
              
                    elif (resFunId1 and not resEndwithSem):
                        if not resFunId2:
                         
                            global flagFun
                            flagFun=1
                            global storeFname
                            func=line.split('(')[0]
                            funcName=func.split()[-1]
							#For Function that is is having parameters in multiple lines
							#If any functionName starts like *FunctionName, then we need to ignore *,so search * and ignore it from FuncName and store in strore1
                            if(re.search(r'^\*.*', funcName)):
                                funcName=funcName[1:]
                            storeFname=funcName.upper()
                            
                            while not (resFunId2):
                                line=file.readline()
                                
                                resFunId2 = re.match(funId2, line)
                            resEndwithSemId=re.match(endwithsemiId,line)
							#If function Decalaration(ends with seicolon) , the we do not want to consider it sp make flagFun=0
                            if(resEndwithSemId):
                                flagFun=0
                        #For function with parameters in a single line
                        global storeFName
                        fun=line.split('(')[0]
                        funName=fun.split()[-1]
                        if(re.search(r'^\*.*', funName)):
                            funName=funName[1:]
                        storeFName=funName.upper()
                        
                        
                        line=file.readline()
                        
                        resComment=re.match(commentId,line)
                        resNewLine=re.match(newlineId,line)
                        
                        while(resNewLine):
                            line=file.readline()
                            resNewLine=re.match(newlineId,line)
                            
                        while(resComment):
                            line=file.readline()
                            resComment=re.match(commentId,line)
                        
                        resFoundFun=re.match(foundfun,line)
                        
                        if(resFoundFun):
                            if (flagFun and storeFname==funcName):
                                myfile.write(storeFname+'FN,\n')
                            elif(flagFun and storeFname!=funcName):
                                myfile.write(storeFname+',\n')
                                flagFun=0
                            elif not flagFun:
							     #checking if the stored function name and the function Name are both in Both Upper case or not, If both are in Upper case ,then we cannot use same name so changing name of stored Function name by adding FN at the end of name
                                if(storeFName==funName):
                                    myfile.write(storeFName+'FN,\n')
                                else:
                                    myfile.write(storeFName+',\n')
                         
                    
                myfile.write('MAX_FUN_NAME\n}eFunName;\n')
                myfile.write('\ntypedef struct profiling\n{\n u32 count;\n u32 timeTaken;\n}tProfiling;\n')
                myfile.write('\nstatic tProfiling arrProfile[MAX_FUN_NAME];\n\n')
                myfile.close()
                
def fun1():
    for cfile in directory1:
        if cfile.endswith(".c"):
            print("InputFile is:"+cfile)
        
            with open(cfile) as file:
                
                name=cfile
                path=directory2+name
                myfile=open(path,'w')
                track=1
                flagLint=0  #To avoid Indentation errors
                for line in file:
                    resInline=re.match(inlineId,line)
                    resFunId1=re.match(funId1,line)
                    resFunId2=re.match(funId2,line)
                    resEndwithSem=re.match(endwithsemicolon,line)
                    resFoundFun=re.match(foundfun,line)
                    resReturn=re.match(returnId,line)
                    resSpace=re.match(spaceId,line)
                    resComment=re.match(endComment,line)
                    resPvtFunc=re.match(pvtFuncId,line) 
                    
                    
                    if(resComment and not flagLint):
                        flagLint=1
                        myfile.write(line)
                        myfile.write('/*lint -e539 */\n/*lint -e525*/\n#include <IfAaSysTime.h>\n')
                       
                
                    elif(resInline):
                            myfile.write(line)
                            while not (resSpace):
                                line=file.readline()
                                myfile.write(line)
                                resSpace=re.match(spaceId,line)
                    
                    elif(resPvtFunc):
                        myfile.write(line)
                        if(track):
                            track=0
                            t=cfile.replace(".c",".txt")
                            path=directory2+t
                            myfile1=open(path,'r')
                            for line1 in myfile1:
                                myfile.write(line1)
                                
                    
                    elif (resFunId1 and not resEndwithSem):
                        
                        if(track):
                            track=0
                            t=cfile.replace(".c",".txt")
                            path=directory2+t
                            myfile1=open(path,'r')
                            for line1 in myfile1:
                                myfile.write(line1)
                        
                        if not resFunId2:
                         
                            global flagFun
                            flagFun=1
                            global storeFname
                            func=line.split('(')[0]
                            funcName=func.split()[-1]
                            if(re.search(r'^\*.*', funcName)):
                                funcName=funcName[1:]
                            storeFname=funcName.upper()
                            while not (resFunId2):
                                myfile.write(line)
                                line=file.readline()
                                resFunId2 = re.match(funId2, line)
                            resEndwithSemId=re.match(endwithsemiId,line)
                            if(resEndwithSemId):
                                flagFun=0
                        
                        myfile.write(line)
                        global storeFName
                        fun=line.split('(')[0]
                        funName=fun.split()[-1]
                        if(re.search(r'^\*.*', funName)):
                            funName=funName[1:]
                        storeFName=funName.upper()
                        line=file.readline()
                        resComment=re.match(commentId,line)
                        resNewline=re.match(newlineId,line)
						
                        while(resNewline):
                            myfile.write(line)
                            line=file.readline()
                            resNewline=re.match(newlineId,line)
                            
                        while(resComment):
                            myfile.write(line)
                            line=file.readline()
                            resComment=re.match(commentId,line)
                        
                        resFoundFun=re.match(foundfun,line)
                        global flagEnd
                        global flagReturn
                        
                        if(resFoundFun):
    
                            flagEnd=1
                            flagReturn=1
                            global flagStartTick
                            
                            if flagStartTick==0:
                               flagStartTick=1 
                               
                            myfile.write(line)
                            myfile.write('\tTAaSysTime64 currentTick = AaTicks64Get();\n')
                        
                        else:
                           myfile.write(line)
                                       
                    elif(resSpace and flagEnd):
                        fun="\t\tarrProfile["
                        r="].timeTaken += AaTicks64Get() - currentTick;"
                        s="].count++;"
                        
                        if(flagReturn and flagFun):
                            if(storeFname==funcName):
                                myfile.write(fun+storeFname+'FN'+r+'\n')
                                myfile.write(fun+storeFname+'FN'+s+'\n')
                                myfile.write(fun+storeFname+'FN].count'+'='+fun+storeFname+'FN].count;'+'\n')
                                myfile.write(line+'\n')
                                flagFun=0
                            else:     
                                myfile.write(fun+storeFname+r+'\n')
                                myfile.write(fun+storeFname+s+'\n')
                                myfile.write(fun+storeFname+'].count'+'='+fun+storeFname+'].count;'+'\n')
                                myfile.write(line+'\n')
                                flagFun=0
								
                        elif(flagReturn and flagFun==0):
                            if(storeFName==funName):
                                myfile.write(fun+storeFName+'FN'+r+'\n')
                                myfile.write(fun+storeFName+'FN'+s+'\n')
                                myfile.write(fun+storeFName+'FN].count'+'='+fun+storeFName+'FN].count;'+'\n')
                                myfile.write(line+'\n')
                            else:
                                myfile.write(fun+storeFName+r+'\n')
                                myfile.write(fun+storeFName+s+'\n')
                                myfile.write(fun+storeFName+'].count'+'='+fun+storeFName+'].count;'+'\n')
                                myfile.write(line+'\n')
                            
                        else:
                            myfile.write(line)
                            flagFun=0
                        
                        flagEnd=0
                        
                    
                    elif(resReturn and flagEnd):
                        flagReturn=0
                        fun="\t\t\t\tarrProfile["
                        r="].timeTaken += AaTicks64Get() - currentTick;"
                        s="].count++;"
                        if(flagFun==1 and storeFname==funcName):
                                myfile.write(fun+storeFname+'FN'+r+'\n')
                                myfile.write(fun+storeFname+'FN'+s+'\n') 
                                myfile.write(fun+storeFname+'FN].count'+'='+fun+storeFname+'FN].count;'+'\n')
                                myfile.write(line+'\n')
                        elif(flagFun==1 and storeFName!=funcName):
                                myfile.write(fun+storeFname+r+'\n')
                                myfile.write(fun+storeFname+s+'\n')
                                myfile.write(fun+storeFname+'].count'+'='+fun+storeFname+'].count;'+'\n')
                                myfile.write(line+'\n')
                        
                        elif(flagFun==0):
                            if(storeFName==funName):
                                myfile.write(fun+storeFName+'FN'+r+'\n')
                                myfile.write(fun+storeFName+'FN'+s+'\n')
                                myfile.write(fun+storeFName+'FN].count'+'='+fun+storeFName+'FN].count;'+'\n')
                                myfile.write(line+'\n')
                            
                            else:    
                                myfile.write(fun+storeFName+r+'\n')
                                myfile.write(fun+storeFName+s+'\n')  
                                myfile.write(fun+storeFName+'].count'+'='+fun+storeFName+'].count;'+'\n')
                                myfile.write(line+'\n')
                    
                    
                    else:
                        myfile.write(line)
                    
                print(name+"\tFile created...Check the Output_Files folder!\n") 
                
            myfile.close()

textFile()
fun1()
                        
                