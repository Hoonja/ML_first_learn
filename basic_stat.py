import time
from scipy import stats

user_product_dic = {}
product_user_dic = {}

product_id_name_dic = {}

for line in open('online_retail_utf.txt'):
    line_items = line.strip().split('\t')
    user_code = line_items[6]
    product_id = line_items[1]
    product_name = line_items[2]

    if len(user_code) == 0:
        continue

    try:
        invoice_year = time.strptime(line_items[4], '%Y-%m-%d %H:%M').tm_year
    except ValueError:
        continue

    if invoice_year != 2011:
        continue

    user_product_dic.setdefault(user_code, set())
    user_product_dic[user_code].add(product_id)

    product_user_dic.setdefault(product_id, set())
    product_user_dic[product_id].add(user_code)

    product_id_name_dic[product_id] = product_name

product_per_user_li = [len(x) for x in user_product_dic.values()]

print('# of users: ', len(user_product_dic))
print('# of products: ', len(product_user_dic))

print(stats.describe(product_per_user_li))
