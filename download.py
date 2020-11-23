from pafy import new
import os
import time

def app():
    for i in range(0,16):
    	print("=>"*i,end=" <=")
    	print("DOWNLOAD   (^o^)",i)
    	
    print("")	
    print("#"*60)
    print("")
    print("(^_~)"*26)
    print("")
    
    time.sleep( 2 )
    os.system("clear")
    print("script by salah eddine elhandaoui ")
    print("سكريبت من طرف صلاح الدين الهنداوي 2020")
    print("#"*30)
    
    print("script for DOwnload any numbers of videos from youtube ")
    print("سكريبت لتحميل اي عدد من الفيديوهات من يوتيوب")
    print("#"*30)
    print("please just guide the steps for DOwnload successfuly")
    print("ارجوك فقط اتبع التعليمات حرفيا")
    print("#"*30)
    print("")
    print("(^o^)"*20)
    print("")
    print("#"*60)
    time.sleep( 3 )
    os.system("clear")
#list of videos
#script by salah eddine elhandaoui 
#script for DOwnload multiple videos from youtube
    videos={}
    try:
        print("ادخل عدد الفيديوهات")
        numvidios=int(input("enter the number of videos url to you want download: ").strip())
        
        if numvidios:
            count=1
            while count<=numvidios:
                print("ادخل رابط الفيديو ",count)
                print("enter video url number  ",count)
                x=input(" => : ").strip()
                print("_"*40)
                videos[count]=x
                count=count+1
    except ValueError:
    	print("please enter number of vidios")
    	print(" ارجوك ادخل قيمة صحيحة لرقم الفيديوهات التي تريد تحميلها")
    


    try:
        url=0
        
        for url in videos:
        
            
            print(videos[url])
            vedio=new(videos[url])
            if vedio:
                print(vedio)
                don=vedio.getbest()
                print("start DOwnloading ..................", videos[url])
                print("بدا تحميل الفيديو انتضر قليلا")
                don.download()

                print("DOwnload successful complete the video url => ",videos[url])
                print("تم تحميل الفيديو بنجاح")
                print("_"*40)
    except ValueError:
            print("error please try again your vidios not download")
            print("لقد حدث خطا ارجوك حاول مرة اخرى لم يتم تحميل اي فيديو")
            
            
    


exit=True
#the call of function
while exit:
    app()
    print("-"*40)
    print("ها تريد الخروج او لا")
    ask=input("if you want exit enter yes if not enter no => ").strip()
    print("-"*40)
    if ask=="no":
        exit=True
    if  ask=="yes":
        exit=False
    else:
        exit=True    
