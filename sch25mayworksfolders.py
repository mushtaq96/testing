from googletrans import Translator
import re
import os
import fnmatch

eng_list = []
#extracting comments from the source file
def sourceComments(filename,string):
    file_lines =[]
    with open(filename,'r',encoding='utf-8')as ro:
        for eachline in ro.readlines():
            if isCommentJapanese(eachline,string)==False:
                file_lines.append(eachline)                
            else:
                string_to_add = translateToEnglish(eachline)#english translation for line
                eng_list.append(string_to_add)
                removeNewlineChar = eachline.rstrip()
                addNewLine = ' '.join([removeNewlineChar,string_to_add,'\n'])
                file_lines.append(addNewLine)

                
                #do it here                    
        print(*eng_list,sep='\n')
        print(len(eng_list))

    with open(filename,'w',encoding='utf-8')as wo:
        wo.writelines(file_lines)
        return True
    return False

    

def isCommentJapanese(single_line,string):
    #is a comment
    if string in single_line:
        #is it japanese
        if(isJapanese(single_line)):
            return True
    return False


#valuidate if japanese character exists
def isJapanese(string):
    clean_string = string.strip()#no use as of now
    clean_string = clean_string.strip('//')#
    #pattern = r'\s{0,}/{2,}\s{0,}[\u3040-\u309f\u30a0-\u30ff\uff66-\uff9f\u4e00-\u9faf]+'
    pattern = r'\s{0,}/{2,}\s{0,}.*[\u3040-\u309f\u30a0-\u30ff\uff66-\uff9f\u4e00-\u9faf]+.*' #match jpn characters in between english
    if re.match(pattern,string):
        return True
    return False

#language conversion of comments to english
def translateToEnglish(jpn_input):
    translator = Translator()
    clean_jpn_input = jpn_input.strip()
    clean_jpn_input = clean_jpn_input.strip('// ')
    pattern = '[\u3040-\u309f\u30a0-\u30ff\uff66-\uff9f\u4e00-\u9faf]+'
    divideJpn = re.findall(pattern,clean_jpn_input) 
    
    if(len(divideJpn)>=1):
        divideJpnString = ''.join(divideJpn)
        eng_output = translator.translate(divideJpnString).text
    else:
        eng_output = translator.translate(clean_jpn_input).text
    return eng_output

#ignore files which end with .cs yet irrelevant
def fnmatching(filename):        
    if fnmatch.fnmatch(filename,'*.Designer.cs'):
        return False
    elif fnmatch.fnmatch(filename,'Temp*.cs'):
        return False
    return True

counter = []
#entry point of the program
def startProgram(path,string):
    
    for ROOT,DIR,FILES in os.walk(path):
        for file in FILES:
            if file.endswith(('cs')) and fnmatching(file):
                
                absolute_path = os.path.join(ROOT,file) 
                if sourceComments(absolute_path,string):
                    counter.append(file)
    return counter
        

                
        
if startProgram('C:\\Users\\b.mushtaq\\testfolder','//'):
    print('\n Comments found')               
    print(counter)
    print("Total relevant c# files -"+str(len(counter)))
else:
    print('\n No comments found')