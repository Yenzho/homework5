import json

def main(path1, path2, path3):
    purchases = {}
    # a = 0
    with open(path1, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            my_dict = json.loads(line)
            dict_key = my_dict["user_id"]
            if my_dict["user_id"] not in purchases.keys():
                purchases.setdefault(my_dict["user_id"], my_dict["category"])
            else:
                purchases[dict_key] = purchases[dict_key] + "," + my_dict["category"]
    with open(path2, encoding='utf-8') as file:
        with open(path3, "w", encoding='utf-8') as wr_file:
            for line in file:
                # if a < 5:
                    line = file.readline().strip().split(',')
                    if line[0] in purchases.keys():
                        line.append(purchases[line[0]])
                        final_line = ','.join(line)
                        wr_file.write(final_line + '\n')
                        # print(final_line)
                        # a += 1

main("Files\\purchase_log.txt","Files\\visit_log.csv","Files\\funnel.csv")














































