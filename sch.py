from googletrans import Translator
import re
import os

#extracting comments from the source file
def sourceComments(filename,string):
    eng_list = []
    with open(filename,'r',encoding='utf-8')as ro:
        for eachline in ro:
            if string in eachline:
                if(isJapanese(eachline)):
                    temp = translateToEnglish(eachline)
                    eng_list.append(temp)

        print(*eng_list,sep='\n')
        print(len(eng_list))


        return True
    return False

#valuidate if it is a comment and is japanese character
def isJapanese(string):
    pattern = r'\s{0,}/{2,}\s{0,}[\u3040-\u309f\u30a0-\u30ff\uff66-\uff9f\u4e00-\u9faf]+'
    if re.match(pattern,string):
        #print("chhh exhstss")
        return True
    return False

#language conversion
def translateToEnglish(jpn_input):
    translator = Translator()
    eng_output = translator.translate(jpn_input).text
    return eng_output



def startProgram(path,string):
    excludes = ['*.vs','.Designer.cs','TemporaryGenerated*.cs']
    for ROOT,DIR,FILES in os.walk(path,topdown=True):
        print (ROOT)
        print (DIR)
        print (FILES)
        # # for file in FILES:
        # #     if file.endswith(('cs')):
        # #         print(file)
        # #     print(len(file))
        # # for directory in DIR:
        # #     if not directory in excludes:
        # #         print(directory)
# if  sourceComments('Schema.cs','//'):
#     print('\n Comments found')
# else:
#     print('\n Try again')
startProgram('C:\\Users\\b.mushtaq\\Desktop\\Code','//')
