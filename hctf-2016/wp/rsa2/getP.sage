import time
from Crypto.Util.number import long_to_bytes,

debug = True

# display matrix picture with 0 and X
def matrix_overview(BB, bound):
    for ii in range(BB.dimensions()[0]):
        a = ('%02d ' % ii)
        for jj in range(BB.dimensions()[1]):
            a += '0' if BB[ii,jj] == 0 else 'X'
            a += ' '
        if BB[ii, ii] >= bound:
            a += '~'

def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):
    """
    Coppersmith revisited by Howgrave-Graham
    
    finds a solution if:
    * b|modulus, b >= modulus^beta , 0 < beta <= 1
    * |x| < XX
    """
    #
    # init
    #
    dd = pol.degree()
    nn = dd * mm + tt

    #
    # checks
    #
    if not 0 < beta <= 1:
        raise ValueError("beta should belongs in (0, 1]")

    if not pol.is_monic():
        raise ArithmeticError("Polynomial must be monic.")

    #
    # calculate bounds and display them
    #
    """
    * we want to find g(x) such that ||g(xX)|| <= b^m / sqrt(n)
    * we know LLL will give us a short vector v such that:
    ||v|| <= 2^((n - 1)/4) * det(L)^(1/n)
    * we will use that vector as a coefficient vector for our g(x)
    
    * so we want to satisfy:
    2^((n - 1)/4) * det(L)^(1/n) < N^(beta*m) / sqrt(n)
    
    so we can obtain ||v|| < N^(beta*m) / sqrt(n) <= b^m / sqrt(n)
    (it's important to use N because we might not know b)
    """
    if debug:
        # t optimized?
        cond1 = RR(XX^(nn-1))
        cond2 = pow(modulus, beta*mm)
        # bound for X
        cond2 = RR(modulus^(((2*beta*mm)/(nn-1)) - ((dd*mm*(mm+1))/(nn*(nn-1)))) / 2)

        # solution possible?
        detL = RR(modulus^(dd * mm * (mm + 1) / 2) * XX^(nn * (nn - 1) / 2))
        cond1 = RR(2^((nn - 1)/4) * detL^(1/nn))
        cond2 = RR(modulus^(beta*mm) / sqrt(nn))


    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)
    
    # construct lattice B
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    # display basis matrix
    if debug:
        matrix_overview(BB, modulus^mm)

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial    
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    # factor polynomial
    potential_roots = new_pol.roots()

    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    # 
    return roots


length_N = 2048;
N = 0x97550b974810279d0c2978ee57241921a6a58b0bfdc9d49e9a9d4fb7acf4fd009b437eeba09aafde864f5c80cac12a393e909e9cdf17a892bd97d88a9040b341a2f82400b202c4653d420d04c3096463b47aed67b6cef2f6b64a49dd0b0c730430f18e2eb6bef65efcb1d8e9608f58a73264eabd00cfe072964402c55d79259223e7c9f4cf19a37751cdb93bb2f839beeeae2492177c2e54d2488df52f45742d7e5560ab797738d83d94b74a32cdff114e76796adb7ecf82aab8d4b10f07f9491605e941645a0a727c4546f32efe41f96a1302ff8f817d9f0efdbd332e3b3a510ca3fc8a2bb2c47b99539183ff768ce05b137cedae791fcb9e905dd8abc3c23dL;

hidden = 384;
qbar = 0xf196cba66507e7b86fe641f243c3cf53a8a09b69456ececbe0998af9b32ab415dc07b2a0a0a72ed8f589f865f4254c113d2952f098e6d6563cf0dcc05e8a77c36d5416738c98722b04c59b4d304a201a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000L; 

F.<x> = PolynomialRing(Zmod(N), implementation='NTL'); 
pol = x - qbar
dd = pol.degree()

# PLAY WITH THOSE:
beta = 0.5                             
epsilon = beta / 7                     
mm = ceil(beta**2 / (dd * epsilon))    
tt = floor(dd * mm * ((1/beta) - 1))   
XX = ceil(N**((beta**2/dd) - epsilon)) 


roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)


q = qbar - roots[0]

print q




