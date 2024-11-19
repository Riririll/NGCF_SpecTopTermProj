# อ่านข้อมูลจาก train.txt และแปลงเป็น train.rating
train_data = []

with open("/content/NGCF_SpecTopTermProj/Data/amazon-book-small/train.txt", "r") as f:
    for line in f.readlines():
        parts = line.strip().split()

        # ID ใหม่ของ user และ item ที่ได้จาก train.txt
        remapped_user_id = int(parts[0])  # userID ใหม่จาก train.txt
        items = list(map(int, parts[1:]))  # itemIDs ใหม่จาก train.txt

        # สำหรับแต่ละ item ที่ผู้ใช้มีการปฏิสัมพันธ์ จะสร้าง triplet (user, item, rating=1)
        for item in items:
            train_data.append((remapped_user_id, item, 1))  # rating=1 สำหรับ positive interaction

# เขียนข้อมูลเป็น train.rating
with open("train.rating", "w") as f:
    for userID, itemID, rating in train_data:
        f.write(f"{userID}\t{itemID}\t{rating}\n")

print(f"Number of training instances: {len(train_data)}")
