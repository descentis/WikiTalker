import wikipediaapi
import time

wiki_wiki = wikipediaapi.Wikipedia('en')


def users(query):
    query = query
    user_list = list()
    page = wiki_wiki.page(f"Talk:{query}/Archive_1")
    num = 1
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
        user_list.append(set(user_in_page))

        print(f"appended users for archive {num}")

        num += 1
        page = wiki_wiki.page(f"Talk:{query}/Archive_{num}")
    page = wiki_wiki.page(f"Talk:{query}")
    if(page.exists()):
        user_main_page = list()
        for key in page.links.keys():
            if('user' in key.lower()):
                if('user talk' not in key.lower()):
                    temp = key
                    user_in_page.append(temp[5:])
                else:
                    temp = key
                    user_in_page.append(temp[10:])
        user_list.append(set(user_main_page))
        print(f"appended users for current talk")

    return user_list


def save_data(query):
    query = query
    page = wiki_wiki.page(f"Talk:{query}/Archive_1")
    num = 1
    # Get total no. of archives in the given article's talk page ###
    archives = len(page.backlinks)-1

    while(page.exists()):
        # Writing archives in the txt file
        for i in page.sections:
            with open(f"{query}_archive.txt", 'a', encoding='utf-8') as f:
                f.write(str(i))

                f.write('\n'*2)
                f.write('#'*40)
                f.write('\n'*2)
                f.close()
        print(f"saved archived : {num} of {archives}")
        num += 1
        page = wiki_wiki.page(f"Talk:{query}/Archive_{num}")

    # For writing the current talk page
    page = wiki_wiki.page(f"Talk:{query}")
    if(page.exists()):
        for k in page.sections:

            with open(f"{query}_archive.txt", 'a', encoding='utf-8') as f:
                f.write(str(k))

                f.close()
        print("written current talk")


def get_date_index(query):
    query = query
    page = wiki_wiki.page(f"Talk:{query}/Archive_1")
    num = 1
    arr = list()
    while(page.exists()):

        page_array = list()
        for i in page.sections:
            temp = list()
            string = str(i)
            for t in range(len(string)-4):
                if(string[t:t+5] == "(UTC)"):
                    temp.append(t)
            page_array.append(temp)
        num += 1
        page = wiki_wiki.page(f"Talk:{query}/Archive_{num}")
        arr.append(page_array)

    page = wiki_wiki.page(f"Talk:{query}")
    if(page.exists()):
        page_array = list()
        for i in page.sections:
            temp = list()
            string = str(i)
            for t in range(len(string)-4):
                if(string[t:t+5] == "(UTC)"):
                    temp.append(t)
            page_array.append(temp)
        arr.append(page_array)

    return arr


def get_date_time(query):
    arr = get_date_index(query)
    query = query
    date_in_pages = list()
    page = wiki_wiki.page(f"Talk:{query}/Archive_1")
    num = 1
    page_index = 0
    while(page.exists()):

        date_in_sections = list()
        for i in range(len(page.sections)):
            temp = list()
            string = str(page.sections[i])
            for j in arr[page_index][i]:
                if ':' in string[j-26:j]:
                    mini_str = string[j-26:j+5]
                    ind = mini_str[::-1].index(':')
                    ind = len(mini_str) - ind - 1

                    temp.append(mini_str[ind-3:j+5])
            date_in_sections.append(temp)
        date_in_pages.append(date_in_sections)
        num += 1
        page = wiki_wiki.page(f"Talk:{query}/Archive_{num}")
        page_index += 1

    page = wiki_wiki.page(f"Talk:{query}")
    if(page.exists()):
        date_in_sections = list()
        for i in range(len(page.sections)):
            temp = list()
            string = str(page.sections[i])
            for j in arr[page_index][i]:
                if ':' in string[j-26:j]:
                    mini_str = string[j-26:j+5]
                    ind = mini_str[::-1].index(':')
                    ind = len(mini_str) - ind - 1

                    temp.append(mini_str[ind-3:j+5])
            date_in_sections.append(temp)
        date_in_pages.append(date_in_sections)

    return arr, date_in_pages


def get_comments():
    comments = list()
    query = input("Article Name: ")
    arr, date_in_pages = get_date_time(query)

    page = wiki_wiki.page(f"Talk:{query}/Archive_1")
    user_list = users(query)
    # section_names = list()
    page_index = 0
    num = 0
    while(page.exists()):
        date_in_sections = date_in_pages[page_index]
        for i, x in enumerate(page.sections):
            section = str(x)
            last_indexes = arr[page_index][i]
            ind = section.index('\n')
            section_name = section[9:ind-4]
            section_dates = date_in_sections[i]
            start_index = ind+1
            for j, y in enumerate(section_dates):
                comment = section[start_index:last_indexes[j]+5]
                user = str()
                for k in user_list[page_index]:
                    if k in comment:
                        user = k
                        break
                date = y
                dic = {
                    'user': user,
                    'comment': comment,
                    'parent_section': section_name,
                    'date_time': date,
                    'article': query
                }
                comments.append(dic)

                start_index = last_indexes[j]+7
        num += 1
        page = wiki_wiki.page(f"Talk:{query}/Archive_{num}")
        page_index += 1

    page = wiki_wiki.page(f"Talk:{query}")
    if(page.exists()):
        date_in_sections = date_in_pages[page_index]
        for i, x in enumerate(page.sections):
            section = str(x)
            last_indexes = arr[page_index][i]
            ind = section.index('\n')
            section_name = section[9:ind-4]
            section_dates = date_in_sections[i]
            start_index = ind+1
            for j, y in enumerate(section_dates):
                comment = section[start_index:last_indexes[j]+5]
                user = str()
                for k in user_list[page_index]:
                    if k in comment:
                        user = k
                        break
                date = y
                dic = {
                    'user': user,
                    'comment': comment,
                    'parent_section': section_name,
                    'date_time': date,
                    'article': query
                }
                comments.append(dic)
                start_index = last_indexes[j]+7

    return comments


query = input("Name: ")

# page = wiki_wiki.page(f"Talk:{query}/Archive_36")

# for i in page.links.keys():
#     if "LordSuryaofShropshire" in i:
#         print('mil gaya madaarchoddd')

save_data(query)