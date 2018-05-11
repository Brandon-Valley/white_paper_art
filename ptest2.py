





#returns bool, is num2 within 10% of num1?
def within_10_percent(num1, num2):
    num1_low  = num1 - (num1 * 0.1)
    num1_high = num1 + (num1 * 0.1)
    
    if   num1_low <= num2 and num2 <= num1:
        return True
    elif     num1 <= num2 and num2 <= num1_high:
        return True
    else:
        return False

def parallel(ra, rb):
    if ra + rb == 0:
        return False
    return (ra * rb) / (ra + rb)





num_answers = 10

A = 10 #gain
VDD = 5

Vss= 0 #GND

min_Vto = 0.8
max_Vto = 1.5

#from data sheet, right?????????????????????
# ID = 0.18
K = 0.05

#for guessing
min_R1 = 1000
max_R1 = 10000

min_R2 = 1000
max_R2 = 1010

min_Rs = 100
max_Rs = 110

min_RD = 100
max_RD = 120 #true max calculated later

# min_R3 = 100
# max_R3 = 120
# 
# min_RL = 100
# max_RL = 101


def calc_gain(R1, R2, Rs, RD,  Vto):
    VG = ( (VDD * R2) + (Vss * R1) ) / (R1 + R2)

    V1 = VG - Vss - Vto

    ID = (  ( ( (1 + 4 * K * V1 * Rs)**(1/2) ) - 1 ) / ( 2 * (K**(1/2)) * Rs)  )**2

    Vs = Vss + (ID * Rs)

    VGS = VG - Vs

#         VDS > VGS - Vto to be in saturation
    max_RD = ( (-VGS + Vto + VDD - Vs) / ID ) - 1
    if (RD > max_RD):
        return False
    
    VD = VDD - (ID * RD)
    
    VDS = VD - Vs
    
    gm = 2 * ( (K * ID)**(1/2) )
    rs = 1 / gm


    A = -RD / rs
    return A


R1 = min_R1
R2 = min_R2
Rs = min_Rs
RD = min_RD
R3 = min_R3
RL = min_RL

#pick R1, R2, Rs, RD, R3, RL
for r1_add in range( max_R1 - min_R1 ):
    R1 += r1_add
    print('%s / %s of the way done...' %(r1_add, max_R1 - min_R1))
    for r2_add in range (max_R2 - min_R2):
        R2 += r2_add
        for rs_add in range( max_Rs - min_Rs ):#find better way to restrict!!!!!!!!!!!!
            Rs += rs_add
            for rd_add in range (max_R1 - min_R2):
                RD += rd_add
#                 for r3_add in range (max_R3 - min_R3):
#                     R3 += r3_add
#                     for rl_add in range (max_RL - min_RL):
#                         RL += rl_add
#                         print('RL: ', RL)
                
                A1 = calc_gain(R1, R2, Rs, RD, min_Vto)
                
                if A1 != False and 9 <= A1 and A1 <= 11:
                    A2 = calc_gain(R1, R2, Rs, RD, max_Vto)  
                    
                    if within_10_percent(A1, A2) == True:
                        print('SUCSESS!')
                        print('R1: ', R1)
                        print('R2: ', R2)
                        print('Rs: ', Rs)
                        print('RD: ', RD)
#                                 print('R3: ', R3)
#                                 print('RL: ', RL)
                        print('gain using Vto = %s: %s' %(min_Vto, A1))
                        print('gain using Vto = %s: %s' %(max_Vto, A2))
                        print(' ')
                        
                        num_answers -= 1
                        if num_answers == 0:
                            print('done!')
                            exit()        
print('no answers found :(')
        
        
        #         Rs = ( ( (K * (ID**3))**(1/2) ) + K * ID * V1 ) / ( K * (ID**2))



d