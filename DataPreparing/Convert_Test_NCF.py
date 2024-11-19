# อ่านข้อมูลจาก test.txt และแปลงเป็น test.rating
test_data = []

with open("/content/NGCF_SpecTopTermProj/Data/amazon-book-small/test.txt", "r") as f:
    for line in f.readlines():
        parts = line.strip().split()

        # ID ใหม่ของ user และ item ที่ได้จาก test.txt
        remapped_user_id = int(parts[0])  # userID ใหม่จาก test.txt
        items = list(map(int, parts[1:]))  # itemIDs ใหม่จาก test.txt

        # สำหรับแต่ละ item ที่ผู้ใช้มีการปฏิสัมพันธ์ จะสร้าง triplet (user, item, rating=1)
        for item in items:
            test_data.append((remapped_user_id, item, 1))  # rating=1 สำหรับ positive interaction

# เขียนข้อมูลเป็น test.rating
with open("test.rating", "w") as f:
    for userID, itemID, rating in test_data:
        f.write(f"{userID}\t{itemID}\t{rating}\n")

print(f"Number of test instances: {len(test_data)}")
