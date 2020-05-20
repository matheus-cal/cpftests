def retira_cpf(cpf):
    format_cpf = ''
    for i in cpf:
        if i.isalnum():
            format_cpf += i      
    
    print(format_cpf)
    return format_cpf


def valida_cpf(num):

    if len(num) < 11:
        return False

    if num in [s * 11 for s in [str(n) for n in range(10)]]:
        return False
    
    try:
        calc = [i for i in range(1, 10)]
        digit1= (sum([int(a)*b for a,b in zip(num[:-2], calc)]) % 11) % 10
        digit2= (sum([int(a)*b for a,b in zip(reversed(num[:-2]), calc)]) % 11) % 10
        num = str(digit1) == num[-2] and str(digit2) == num[-1]
        return num
    except ValueError:
        return False

