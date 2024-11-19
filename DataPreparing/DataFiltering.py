import os
import pandas as pd
import numpy as np
import scipy.sparse as sp
import random

def filter_amazon_book(data_path, n_users=1000, n_items=7000, min_interactions=5):
    # อ่านไฟล์ train.txt
    with open(f"{data_path}/train.txt", 'r') as f:
        lines = f.readlines()

    # แปลงข้อมูลเป็น DataFrame
    interactions = []
    for line in lines:
        parts = line.strip().split()  # split() จะแยกตามช่องว่าง
        user = int(parts[0])          # user_id คือตัวแรก
        items = list(map(int, parts[1:]))  # item_ids คือรายการที่เหลือ
        for item in items:
            interactions.append([user, item])

    df = pd.DataFrame(interactions, columns=['user_id', 'item_id'])

    # นับจำนวน interactions ต่อ user และ item
    user_counts = df['user_id'].value_counts()
    item_counts = df['item_id'].value_counts()

    # เลือก users และ items ที่มี interactions มากที่สุด
    selected_users = user_counts[user_counts >= min_interactions].head(n_users).index
    selected_items = item_counts[item_counts >= min_interactions].head(n_items).index

    # กรองข้อมูลให้เฉพาะ users และ items ที่เลือก
    filtered_df = df[
        (df['user_id'].isin(selected_users)) &
        (df['item_id'].isin(selected_items))
    ]

    # สร้าง mapping ใหม่สำหรับ user_id และ item_id
    user_map = {old_id: new_id for new_id, old_id in enumerate(sorted(filtered_df['user_id'].unique()))}
    item_map = {old_id: new_id for new_id, old_id in enumerate(sorted(filtered_df['item_id'].unique()))}

    # แปลง IDs
    filtered_df['user_id'] = filtered_df['user_id'].map(user_map)
    filtered_df['item_id'] = filtered_df['item_id'].map(item_map)

    return filtered_df, user_map, item_map


def filter_test_file(test_file, user_map, item_map, output_test_file):
    # อ่านไฟล์ test.txt
    with open(test_file, 'r') as f:
        lines = f.readlines()

    test_interactions = []
    for line in lines:
        parts = line.strip().split()  # split() จะแยกตามช่องว่าง
        user = int(parts[0])          # user_id คือตัวแรก
        items = list(map(int, parts[1:]))  # item_ids คือรายการที่เหลือ
        for item in items:
            if user in user_map and item in item_map:  # กรองเฉพาะ user และ item ที่อยู่ใน mapping
                test_interactions.append([user_map[user], item_map[item]])

    # สร้าง DataFrame จากข้อมูลที่กรองแล้ว
    test_df = pd.DataFrame(test_interactions, columns=['user_id', 'item_id'])

    # บันทึกข้อมูลใน test.txt
    test_data = test_df.groupby('user_id')['item_id'].agg(list)
    with open(output_test_file, 'w') as f:
        for user_id, items in test_data.items():
            items_str = ' '.join(map(str, items))  # เปลี่ยนจากคอมม่าเป็นช่องว่าง
            f.write(f"{user_id} {items_str}\n")


# สร้างไฟล์ใหม่
def save_filtered_data(filtered_df, user_map, item_map, output_path):
    # สร้าง train.txt
    train_data = filtered_df.groupby('user_id')['item_id'].agg(list)
    with open(f"{output_path}/train.txt", 'w') as f:
        for user_id, items in train_data.items():
            items_str = ' '.join(map(str, items))  # เปลี่ยนจากคอมม่าเป็นช่องว่าง
            f.write(f"{user_id} {items_str}\n")

    # สร้าง user_list.txt
    with open(f"{output_path}/user_list.txt", 'w') as f:
        for old_id, new_id in user_map.items():
            f.write(f"{old_id} {new_id}\n")  # ใช้ช่องว่างเป็นตัวคั่น

    # สร้าง item_list.txt
    with open(f"{output_path}/item_list.txt", 'w') as f:
        for old_id, new_id in item_map.items():
            f.write(f"{old_id} {new_id}\n")  # ใช้ช่องว่างเป็นตัวคั่น

# กรองและบันทึกข้อมูล
data_path = "/content/NGCF_SpecTopTermProj/Data/amazon-book"
output_path = "/content/NGCF_SpecTopTermProj/Data/amazon-book-small"

# สร้างโฟลเดอร์ใหม่
os.makedirs(output_path, exist_ok=True)

# กรองข้อมูลใน train.txt
filtered_df, user_map, item_map = filter_amazon_book(data_path)
save_filtered_data(filtered_df, user_map, item_map, output_path)

# กรองและบันทึกข้อมูลใน test.txt
test_file = f"{data_path}/test.txt"
output_test_file = f"{output_path}/test.txt"
filter_test_file(test_file, user_map, item_map, output_test_file)
