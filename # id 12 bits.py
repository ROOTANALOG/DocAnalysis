# id 10 bits 
import itertools
if __name__ == "__main__":
    year = input("Please input born year：")
    months = [ '01','02','03','04','05','06','07','08','09','10','11','12']
    dates = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

    # dateHead = []
    # for month in months:
    #     for date in dates:
    #         unitday = month + date
    #         dateHead.append(unitday)



    other = '0123456789'  #第15-16位
    check = '0123456789X' #第18位
    sex = '02468' if int(input("请输入性别（男1女2）："))%2 == 0 else '13579' #第17位
    nums = itertools.product(months, dates, other,other,sex,check)
    cards = []
    for num in nums:
        #for unitday in dateHead:
            card = year + "".join(num)
            cards.append(card+'\n')
with open ('身份证后12位字典.txt','w',encoding='utf-8') as f:
    for each in cards:
        f.write(each)
