import math
class Sol:
    def is_pow_of_3(self,num):
        max_int=2**31-1
        max_pow=int(math.log(max_int,3))
        return 3**max_pow%num==0
if __name__ == '__main__':
    p1=Sol()
    print(p1.is_pow_of_3(28))
