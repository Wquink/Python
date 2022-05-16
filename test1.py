def phonenumber(digits):
    if not digits:
        return []
    keyboard = {
        "2":'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }
    res = []
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return keyboard[digits]
    restult = phonenumber(digits[1:])   #在函数内部调用函数
    for i in restult:
        for j in keyboard[digits[0]]:
            res.append((j+i))

    return res

print(phonenumber('23'))

print(phonenumber('99'))