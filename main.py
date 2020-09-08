import json
from algo.apriori_algo import AprioriAlgo


def main():
    f = open('test_data.json')
    data = json.load(f)

    list_data = []

    for piece in data:
        recent_list_tag = []
        cnt_tag = 0
        for tag in piece['tag']:
            normalize_tag = tag.strip().upper()
            recent_list_tag.append(normalize_tag)
            cnt_tag += 1
        list_data.append(recent_list_tag)

    print('Build set_tag ok')

    f.close()

    algo = AprioriAlgo(db=list_data, minsup=0.1)

    f = open("result.json", "w")
    f.write(json.dumps(algo.list_res_candidate))
    f.close()


def ext_gcd(a,b):
    m, n = a, b
    xm, ym = 1, 0
    xn, yn = 0, 1
    while n != 0:
        q = m // n # chia lấy phần nguyên
        r = m % n # chia lấy phần dư
        xr, yr = xm - q*xn, ym - q*yn
        m = n
        xm, ym = xn, yn
        n = r
        xn, yn = xr, yr
    return xm, ym# m = gcd(a,b) = xm * a + ym * b

print( ext_gcd(43, 19) )
