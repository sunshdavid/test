def SET_PWM(io1,io2,p1,p2,p3,p4):
    buf = [0x20]
    if(io1==0):
        buf+=[0x30]
    elif(io1==1):
        buf+=[0x04]
    elif(io1==3):
        buf+=[0x00]
    if(io2==0):
        buf+=[0x40]
    elif(io2==1):
        buf+=[0x04]
    elif(io2==3):
        buf+=[0x00]

    buf+=[(0xff00 & p1)>>8]
    buf+=[(0x00ff & p1)]
    buf+=[(0xff00 & p2)>>8]
    buf+=[(0x00ff & p2)]
    buf+=[(0xff00 & p3)>>8]
    buf+=[(0x00ff & p3)]
    buf+=[(0xff00 & p4)>>8]
    buf+=[(0x00ff & p4)]


    print(buf)



def GET_PWM():
    buf = [0x22]
    buf += [0X00]*8
    s= spi.xfer2(buf)
    return s[2:8]

def CAN_SEND(ID,TYPE,DATA,n):
    buf = [0x42]
    buf+=[(0xff00 & ID)>>8]
    buf+=[(0x00ff & ID)]
    buf+=[0xff & TYPE]
    for i in range(0,n):
        buf+=[DATA[i]]
    #spi.xfer2(buf)


def CAN_RECV():
    buf = [0x41]
    buf += [0X00]*12
    #s=spi.xfer2(buf)


def RF_SEND(addr,data,n):
    buf = [0x32]
    buf+=[(0xff00 & addr)>>8]
    buf+=[(0x00ff & addr)]
    buf+=[0xff & n]
    for i in range(0,n):
        buf+=[data[i]]
    #spi.xfer2(buf)
    print(buf)


def RF_RECV():
    buf = [0x41]
    buf += [0X00] * 29
    #s = spi.xfer2(buf)
    #return s[2:s[2]]


d=[0x00]
for i in range(1,20):
    d+=[i]
RF_SEND(0x1233,d,20)

