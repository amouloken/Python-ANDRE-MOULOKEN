import datetime
print("Birthday Calculator\n")
while(1):
        name = input("Enter name: ")
        birthday = input("Enter birthday (MM/DD/YY): ")
 
        list = []
        list = birthday.split('/')
        mm = int(list[0]);
        dd = int(list[1])
        yy = int(list[2])
 
        c=19;
        if(yy<10):
                 c=200;
        elif(yy<=18):
                 c=20;
        yy = int(str(c)+str(yy))
 
        w = datetime.date(yy, mm, dd);
        print("Birthday: "+ w.strftime("%A")+", "+w.strftime("%B")+" "+w.strftime("%d")+", "+str(w.year))
        x = datetime.date.today()
        print("Today: "+ x.strftime("%A")+", "+x.strftime("%B")+" "+x.strftime("%d")+", "+str(x.year))
 
        years_diff = x.year - yy;
        days_diff = 0;
        if(mm>x.month):
                years_diff = years_diff-1;
                y = datetime.date(x.year, mm, dd)
                diff = y-x;
                days_diff = diff.days;
        elif(mm==x.month):
                if(dd>x.day):
                        years_diff = years_diff-1;
                        days_diff = dd-x.day;
                elif(dd<x.day):
                        if(dd==x.day-1):
                                days_diff=-1;
                        else:
                                y = datetime.date(x.year+1, mm, dd)
                                diff = y-x;
                                days_diff = diff.days;
        else:
                y = datetime.date(x.year+1, mm, dd)
                diff = y-x;
                days_diff = diff.days;
                if(years_diff<2):
                    print(name+" is "+str(years_diff*365+365-days_diff)+" days old.")
                else:
                    print(name+" is "+str(years_diff)+" years old.")
                s = ""
                if(days_diff==0):
                    s="is today!"
                elif(days_diff==1):
                    s="is tomorrow!"
                elif(days_diff==-1):
                    s="was yesterday!"
                else:
                    s="is in "+str(days_diff)+" days.";
                print(name+"'s birthday "+s+"\n")
                option = input("Continue? (y/n): ")
                if(option=='n'):
                    break;

