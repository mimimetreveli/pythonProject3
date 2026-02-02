# coding=utf-8
from itertools import count

with open("titanic") as obj:
    info={
        "passengers_amount":{

        },
        "alive_passengers_amount":{

        },
        "dead_passengers_amount":{

        },
        "class_of_tickets":{
            "first_class":{

            },
            "second_class":{

            },
            "third_class":{

            }
        }
    }
    obj.readline()
    num_of_f=0
    num_of_m=0
    alive_f=0
    alive_m=0
    first_class=0
    second_class=0
    third_class=0
    fairs_first = []
    fairs_second = []
    fairs_third = []
    for line in obj:
        parts=line.strip().split(",")
        if parts[4]=="female" and int(parts[1])==1:
            num_of_f+=1
            alive_f+=1
        elif parts[4] == "female":
                num_of_f += 1
        elif parts[4]=="male" and int(parts[1])==1:
            num_of_f+=1
            alive_m+=1
        else:
            num_of_m+=1
        if int(parts[2])==1:
            first_class+=1
            fairs_first.append(float(parts[9]))
        elif int(parts[2])==2:
            second_class+=1
            fairs_second.append(float(parts[9]))
        else:
            third_class+=1
            fairs_third.append(float(parts[9]))
    pr_f=num_of_f*100/(num_of_m+num_of_f)
    pr_m=num_of_m*100/(num_of_f+num_of_m)
    info["passengers_amount"]["female"]=num_of_f
    info["passengers_amount"]["female_%"]=pr_f
    info["passengers_amount"]["male"]=num_of_m
    info["passengers_amount"]["male_%"]=pr_m
    info["alive_passengers_amount"]["female"]=alive_f
    info["alive_passengers_amount"]["male"]=alive_m
    info["alive_passengers_amount"]["female_%"]=alive_f*100/num_of_f
    info["alive_passengers_amount"]["male_%"]=alive_m*100/num_of_m
    info["dead_passengers_amount"]["female"]=num_of_f-alive_f
    info["dead_passengers_amount"]["male"]=num_of_m-alive_m
    info["dead_passengers_amount"]["female_%"]=100-(alive_f * 100 / num_of_f)
    info["dead_passengers_amount"]["male_%"]=100-(alive_m*100/num_of_m)
    info["class_of_tickets"]["first_class"]["amount"]=first_class
    info["class_of_tickets"]["second_class"]["amount"] = second_class
    info["class_of_tickets"]["third_class"]["amount"] = third_class
    info["class_of_tickets"]["first_class"]["average_of_fairs"] = sum(fairs_first)/first_class
    info["class_of_tickets"]["second_class"]["average_of_fairs"] = sum(fairs_second) / second_class
    info["class_of_tickets"]["third_class"]["average_of_fairs"] = sum(fairs_third) / third_class
    info["class_of_tickets"]["first_class"]["amount_%"] = first_class*100/(first_class+second_class+third_class)
    info["class_of_tickets"]["second_class"]["amount_%"] = second_class*100/(first_class+second_class+third_class)
    info["class_of_tickets"]["third_class"]["amount_%"] = third_class*100/(first_class+second_class+third_class)
    # print("number of females: ",num_of_f)
    # print("percentage of females: ", pr_f)
    # print("number of males: ",num_of_m)
    # print("percentage of males: ", pr_m)
    # print("number of females who survived: ", alive_f)
    # print("number of females who did not survive: ",num_of_f-alive_f)
    # print("percentage of females who survived", alive_f*100/num_of_f)
    # print("percentage of females who did not survive", 100-(alive_f * 100 / num_of_f))
    # print("number of males who survived: ", alive_m)
    # print("number of males who did not survive: ",num_of_m-alive_m)
    # print("percentage of males who survived", alive_m*100/num_of_m)
    # print("percentage of males who did not survive", 100 - (alive_m * 100 / num_of_m))
    # print("number and percentage of first class tickets: ",first_class,first_class*100/(first_class+second_class+third_class))
    # print("number and percentage of second class tickets: ",second_class, second_class*100/(first_class+second_class+third_class))
    # print("number and percentage of third class tickets: ",third_class, third_class*100/(first_class+second_class+third_class))
    # print("average of first class tickets' fairs", sum(fairs_first)/first_class)
    # print("average of second class tickets' fairs", sum(fairs_second) / second_class)
    # print("average of third class tickets' fairs", sum(fairs_third) / third_class)
#1: read_mode,write_mode,append_mode,read/write_mode,append/read_mode
#2: შეიქმნება ახალი ფაილი მიცემული სახელით
#3: list ცვლადია და tuple უცვლადია
#4: key