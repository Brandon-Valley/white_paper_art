





#returns bool, is num2 within 10% of num1?
def within_10_percent(num1, num2):
    if num1 == False or num2 == False:
        return False
    
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









def calc_gain(R1_, R2, Rs, RD,  Vto):
    VG = ( (VDD * R2) + (Vss * R1_) ) / (R1_ + R2)

    V1 = VG - Vss - Vto

    ID = (  ( ( (1 + 4 * K * V1 * Rs)**(1/2) ) - 1 ) / ( 2 * (K**(1/2)) * Rs)  )**2

    Vs = Vss + (ID * Rs)

    VGS = VG - Vs

#         VDS > VGS - Vto to be in saturation
    max_RD = ( (-VGS + Vto + VDD - Vs) / ID )
    if (RD >= max_RD):
        print('RD too big, %s < %s == false' %(RD, max_RD))
        return False
    
    VD = VDD - (ID * RD)
    
    VDS = VD - Vs
    
    gm = 2 * ( (K * ID)**(1/2) )
    rs = 1 / gm


    A = RD / rs
    return A







num_answers = 10

A = 10 #gain
VDD = 5

Vss= 0 #GND

min_Vto = 0.8
max_Vto = 1.5

#from data sheet
K = 0.05


#choose
ID = 0.003#0.006
Rs_start = 0.01
R2 = 800


RD = (A) / ( 2 * ((K * ID)**(1/2)) )


def calc_R1(Rs_, Vto_):
    VG = Vss + Vto_ +( -( ((K*ID)**(1/2)) - (K * ID * Rs_) ) / K )
    
    #make sure its in saturation
    if VG >= VDD - (ID * Rs_):
        print('not in saturation, VG: %s >= %s'%(VG, VDD - (ID * Rs_) ))
        return False
    
    R1 = ( (VDD * R2) / VG ) - R2
    return R1
    


# R1 = calc_R12(Rs_start, min_Vto)


Rs_try = Rs_start
R1_try = calc_R1(Rs_try, max_Vto)
A_try = calc_gain(R1_try, R2, Rs_try, RD, max_Vto)

while(within_10_percent(A, A_try) == False or within_10_percent(A, calc_gain(R1_try, R2, Rs_try, RD, min_Vto)) == False or R1_try == False):
    Rs_try += 1
    print('Rs: ', Rs_try)
    R1_try = calc_R1(Rs_try, max_Vto)
    A_try  = calc_gain(R1_try, R2, Rs_try, RD, max_Vto)
    print('    A:', A_try)
    print('        A with min_Vto = ', calc_gain(R1_try, R2, Rs_try, RD, min_Vto))
    
print('SUCSESS!')
print('R1: ', R1_try)
print('R2: ', R2)
print('Rs: ', Rs_try)
print('RD: ', RD)
print('gain using Vto = %s: %s' %(min_Vto, calc_gain(R1_try, R2, Rs_try, RD, min_Vto)))
print('gain using Vto = %s: %s' %(max_Vto, A_try))
# print('Just for confirmation, gain with min_Vto: ', calc_gain(R1_try, R2, Rs_try, RD, min_Vto) )




