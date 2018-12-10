# with open("../sqlSentence/nav_li.txt", "r") as f:
#     for iter in f:
#         iter = eval(iter)
#         with open ("../sqlSentence/nav_li_sql.txt", "a+") as fj:
#             cat_id = iter["custom"]["cat_id"]
#             a_index = iter["custom"]["index"].split("_")[0]
#             b_index = iter["custom"]["index"].split("_")[1]
#             title = iter["custom"]["title"]
#             fj.write("insert into nav_li values("+str(cat_id)+", "+a_index+", "+b_index+", \'"+title+"\', "+"1"+");"+"\n")

num = 0
with open("../sqlSentence/detail_content.txt", "r") as f:
    for iter in f:
        iter = eval(iter)
        with open("../sqlSentence/detail_content_sql.txt", "a+") as fj:
            id = num
            try:
                cat_id = iter["custom"]["cat_id"]
            except:
                cat_id = 0
            a_index = iter["custom"]["index"].split("_")[0]
            b_index = iter["custom"]["index"].split("_")[1]
            c_index = iter["custom"]["index"].split("_")[2]
            title = iter["custom"]["title"]
            fj.write("insert into detail_content values(" +str(id) + ", "+ str(
                cat_id) + ", " + a_index + ", " + b_index + ", "+ c_index + ", \'" + title + "\', " + "1" + ");" + "\n")

        num += 1