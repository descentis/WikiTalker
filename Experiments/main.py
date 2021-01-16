import wikipediaapi
import time
import json
wiki_wiki = wikipediaapi.Wikipedia('en')


def main():
    query = input("Article Name : ")
    page = wiki_wiki.page(f"Talk:{query}/Archive_1")
    num = 1
    comments = dict()
    comments['data'] = list()
    parse_time = 0
    while(page.exists()):
        user_in_page = list()
        for key in page.links.keys():
            if('user' in key.lower()):
                if('user talk' not in key.lower()):
                    temp = key
                    user_in_page.append(temp[5:])
                else:
                    temp = key
                    user_in_page.append(temp[10:])

        for x in page.sections:
            start_time = time.time()
            section = str(x)

            ind = section.index('\n')
            section_name = section[9:ind-4]
            start_index = ind+1
            for t in range(len(section)-4):
                if(section[t:t+5] == "(UTC)"):
                    if ':' in section[t-26:t]:
                        mini_str = section[t-26:t+5]
                        date = mini_str[::-1].index(':')
                        date = len(mini_str) - date - 1
                        final_date = mini_str[date-3:t+5]
                        comment = section[start_index:t+5]
              
            
                        user = str()
                        for k in user_in_page:
                            if k in comment:
                                user = k
                                break
                        split_arr = comment.split('\n')
                        comment = " ".join(split_arr)
                        comment = comment[:comment.index(user)]
                        # if user != "":

                        if "Preceding unsigned comment added by" in comment:
                            comment.replace(
                                "Preceding unsigned comment added by", "")

                        dic = {
                            'user': user,
                            'comment': comment,
                            'parent_section': section_name,
                            'date_time': final_date,

                        }
                        comments['data'].append(dic)
                        start_index = t+5
            end_time = time.time()
            diff_time = end_time - start_time
            parse_time += diff_time
        print(f"Saved data for archive {num}")
        num += 1
        page = wiki_wiki.page(f"Talk:{query}/Archive_{num}")

    page = wiki_wiki.page(f"Talk:{query}")
    if page.exists():
        user_in_page = list()
        for key in page.links.keys():
            if('user' in key.lower()):
                if('user talk' not in key.lower()):
                    temp = key
                    user_in_page.append(temp[5:])
                else:
                    temp = key
                    user_in_page.append(temp[10:])

        for x in page.sections:
            start = time.time()

            section = str(x)

            ind = section.index('\n')
            section_name = section[9:ind-4]
            start_index = ind+1
            for t in range(len(section)-4):
                if(section[t:t+5] == "(UTC)"):
                    if ':' in section[t-26:t]:
                        mini_str = section[t-26:t+5]
                        date = mini_str[::-1].index(':')
                        date = len(mini_str) - date - 1
                        final_date = mini_str[date-3:t+5]
                        comment = section[start_index:t+5]
       
                        user = str() 
                        for k in user_in_page:
                            if k in comment:
                                user = k
                                break
                        split_arr = comment.split('\n')
                        comment = " ".join(split_arr)
                        comment = comment[:comment.index(user)]
                        # if user != "":

                        if "Preceding unsigned comment added by" in comment:
                            comment.replace(
                                "Preceding unsigned comment added by", "")

                        dic = {
                            'user': user,
                            'comment': comment,
                            'parent_section': section_name,
                            'date_time': final_date,
                        }

                        comments['data'].append(dic)

                        start_index = t+5

            end = time.time()
            diff = end - start
            parse_time += diff
    print(f"saved data for the current talk page")
    json_data = json.dumps(comments, indent=4)
    with open(f'./output_json/{query}.json', 'w') as f:
        f.write(json_data)
        f.close()
    return parse_time


start = time.time()
parse_time = main()
stop = time.time()

print("Execution Time:", stop-start)
print("pasre time:", parse_time)

