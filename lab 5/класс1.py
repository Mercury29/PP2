import re

def t1(s):
    p = r'^ab*$'
    return bool(re.match(p, s))

def t2(s):
    p = r'^ab{2,3}$'
    return bool(re.match(p, s))

def t3(s):
    p = r'[a-z]+_[a-z]+'
    return re.findall(p, s)

def t4(s):
    p = r'\b[A-Z][a-z]+\b'
    return re.findall(p, s)

def t5(s):
    p = r'^a.*b$'
    return bool(re.match(p, s))

def t6(s):
    return re.sub(r'[ ,\.]', ':', s)

def t7(s):
    a = s.split('_')
    return a[0] + ''.join(x.capitalize() for x in a[1:])

def t8(s):
    return re.split(r'(?=[A-Z])', s)

def t9(s):
    p = r'\b[A-Z][a-z]*\b'
    return re.findall(p, s)

def t10(s):
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', s)
    s2 = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.lower()

def main():
    try:
        with open("row.txt", "r", encoding="cp1251") as f:
            txt = f.read()
    except FileNotFoundError:
        print("row.txt not found!")
        return

    ln = txt.splitlines()

    print("1.")
    for l in ln:
        if t1(l):
            print(l)

    print("\n2.")
    for l in ln:
        if t2(l):
            print(l)

    print("\n3.", t3(txt))
    print("\n4.", t4(txt))

    print("\n5.")
    for l in ln:
        if t5(l):
            print(l)

    print("\n6.", t6(txt))
    print("\n7.", t7("example_snake_case_text"))
    if ln:
        print("\n8.", t8(ln[0]))
    print("\n9.", t9(txt))
    print("\n10.", t10("CamelCaseExampleText"))

if __name__ == "__main__":
    main()
