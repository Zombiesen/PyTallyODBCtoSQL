import tally_core as tc

def import_sql(sql_string_dict):
    try:
        file1 = open('custom_sql.txt')
        count = 0
        while True:
            count += 1
            line = file1.readline()
            
            if not line:
                break

            line = line.rstrip("\n")
            firstName, _, lastName = line.partition(':')
            # if is_strinlastName
            sql_string_dict.update({firstName:lastName})

        file1.close()
    except Exception as e:
        print(e)

    return sql_string_dict
