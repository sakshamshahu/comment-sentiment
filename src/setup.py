import pandas as pd 
import numpy as np

comments_df = pd.read_csv("/home/saksham/AVI/Projects/Sentiment-Comments/data/raw/Comments.csv",encoding='cp1252')
positive_df = pd.read_csv("data/raw/positive-words.csv")
negative_df = pd.read_csv("data/raw/negative-words.csv",encoding='cp1252')
commentss = comments_df["Comments"].to_numpy()

# splited = np.char.split(commentss[1])
n = commentss.size
positive_arr =positive_df["Positive Words"].to_numpy()
negative_arr = negative_df["Negative Words"].to_numpy()

# print(splited)
# size_splited = splited.size
# print(size_splited)
positive_count_list = []

for i in range (0,2):
    positive_count =0
    lower_case = np.char.lower(commentss[i])
    splited = np.char.split(lower_case)
    split_list = splited.tolist()
    list_length = len(split_list)
    print(list_length)
    for j in range (0,list_length):
        for k in range (0,positive_arr.size):
            if split_list[j] == positive_arr[k]:
                positive_count += 1
    positive_count_list.insert(i,positive_count)

print(positive_count_list)
print(len(positive_count_list))

# negative_count_list =[]


# for i in range (0,n):
#     negative_count =0
#     lower_case = np.char.lower(commentss[i])
#     splited = np.char.split(lower_case)
#     split_list = splited.tolist()
#     list_length = len(split_list)
#     for j in range (0,list_length):
#         for k in range (0,negative_arr.size):
#             if split_list[j] == negative_arr[k]:
#                 negative_count += 1
#     negative_count_list.insert(i,negative_count)

# print(negative_count_list)
# print(len(negative_count_list))

# comments_df["positive"] =np.array(positive_count_list)
# comments_df["negative"] =np.array(negative_count_list)
# print(comments_df)

# comments_df.to_csv("/home/saksham/AVI/Projects/Sentiment-Comments/data/raw/UpdatedComments.csv")
# comments_df.to_excel("/home/saksham/AVI/Projects/Sentiment-Comments/data/raw/UpdatedComments.xlsx", sheet_name="Testing", index=False)