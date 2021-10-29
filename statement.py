# find the word count, letter count, line count and integer count in the givenstatement
#
#
# statement="""Within the text of most pages, there are usually 44 many hypertext links to other pages within the wiki.
# This form of non-linear navigation is more "native" to a wiki 12 than structured/formalized navigation 134 schemes.
# Users can also create any number of index or table-of-contents 433 pages, with hierarchical categorization 44 or whatever form of organization they like."""
# char_count=0
# lst=[]
# words = statement.split()
# for i in words:
#     if i.isdigit():
#         lst.append(i)
#     else:
#         char_count+=len(i)
#
# print("char_count : ",char_count)
# print(f"Word_count:{len(words)}")
# print((f"Line count:{len(statement.splitlines())}"))
# print(f"Integer count {len(lst)}")



# output
# """wHoah earah uyoah inikkah
# Iah maah dgooah eherah
# syourah ylovinglah amunnah"""
# every word last character to be moved to first
# and ah to be added to the last


# s="""How are you nikki
# I am good here
# yours lovingly munna"""
# # words=str1.split()
# # lst=[]
# # for i in words:
# #     lst.append( i[-1]+i[:-1]+'ah')
# # print(" ".join(lst))
#
# lines = s.splitlines()
# result = []
# for line in lines:
#     words = line.split()
#     out = []
#     for word in words:
#         out.append(word[-1]+word[:-1]+"ah")
#     result.append(" ".join(out))
# print("\n".join(result))
# print(result)


s="""How are you nikki
I am good here
yours lovingly munna"""
#
# words = []
# start_pos, end_pos = 0, 0
# for i in range(len(s)):
#    if s[i] == " ":
#        words.append(s[start_pos: end_pos])
#        start_pos = end_pos
#    end_pos += 1
# else:
#     words.append(s[start_pos: end_pos])
# print(words)

words = []
start_pos, end_pos = 0, 0
s = s.replace("\n"," ")
for i in range(len(s)):
   if s[i] ==" ":
       words.append(s[start_pos: end_pos])
       start_pos = end_pos
   end_pos += 1
else:
    words.append(s[start_pos: end_pos])
print(words)
