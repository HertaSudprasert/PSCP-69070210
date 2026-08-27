"""arcade of time"""
def main():
    """stain of time"""
    fst_para=input().split(" ")
    num_of_ran=int(fst_para[0])
    mex_range=int(fst_para[1])
    list_open=[]
    list_close=[]
    list_time=[]
    ran=0
    timer=0
    for _ in range(num_of_ran):
        data = input().split(" ")
        list_open.append(int(data[0]))
        list_close.append(int(data[1]))
    sec_para=input().split(" ")
    for _ in range(mex_range):
        timer=0
        for ran in range(num_of_ran):
            if list_open[ran]<=int(sec_para[_])<list_close[ran]:
                timer+=1
        list_time.append(timer)
    print(*list_time)
main()
