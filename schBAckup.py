from googletrans import Translator


def checkComments(filename,string):
    comlst = []
    with open(filename,'r',encoding='utf-8')as ro:
        for eachline in ro:
            if string in eachline:
                comlst.append(eachline)
        print(*comlst,sep='\n')
        print(len(comlst))
        translate(comlst)
        
        return True
    return False


def translate(total_comments):
    translst = []
    for each_comment in total_comments:
        resp = googleApi(each_comment)
        translst.append(resp)
    print(*translst,sep='\n')
    print(len(translst))


def googleApi(source_text):
    translator = Translator()
    return translator.translate(source_text).text
    




if checkComments('Schema.cs','//'):
    print('\n Comments found')

else:
    print('\n Try again')
