


def convert_decimal_to_roman(decimal_number):
    roman = ''
    
    rest = decimal_number % 10
    mult_10 = decimal_number // 10
    result_1 = ''
    result_2 = ''
    result_3 = ''
    result_4 = ''
    result_5 = ''
    result_6 = ''
    result_7 = ''
    result_10 =''
    result_11 = ''
    result_12 = ''
    result_13 = ''
    result_14 = ''
    if 0<mult_10 <4:
        for digit in range(mult_10):
            result_1 += 'X'

    if mult_10 == 4 :
        for digit in range(1):
            result_12 = 'XL'

    if 5<=mult_10 <9:
        for digit in range(1):
            result_10 = 'L'
        for digit in range(mult_10-5):
            result_11 += 'X'
    if mult_10 == 9 :
        for digit in range(1):
            result_13 = 'XC'
    if mult_10 == 10:
        for digit in range(1):
            result_14= 'C'


    if rest < 4:
        for digit in range(rest):
            result_2 += 'I'
    if rest == 5:
        for digit in range(1):
            result_3 = 'V'
    if rest == 4 :
        for digit in range(1):
            result_6 += 'IV'
    if rest == 9 :
        for digit in range(1):
            result_5 += 'IX'
    if 5<=rest<9:
        for digit in range(1):
            result_3 = 'V'
        for digit in range(rest-5):
            result_7 += 'I'
       
            

        
    
  

    result = result_10+result_11+result_12+result_13+result_14+result_1 + result_2 +result_3+result_4+result_5+result_6+ result_7
    return result

