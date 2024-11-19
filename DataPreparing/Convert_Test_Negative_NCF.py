import random

num_items = 7000  # จำนวนไอเท็มทั้งหมด

# ฟังก์ชันอ่านไฟล์ test.rating และสร้าง dictionary ที่เก็บ positive items
def load_test_rating(file_path):
    test_data = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split("\t")
            userID = int(parts[0])  # userID
            itemID = int(parts[1])  # itemID
            rating = float(parts[2])  # rating
            if userID not in test_data:
                test_data[userID] = set()
            test_data[userID].add(itemID)
    return test_data

# ฟังก์ชันสร้าง negative samples จาก positive items
def create_negative_samples(test_data, num_items):
    negative_samples = []
    for userID, pos_items in test_data.items():
        # สำหรับแต่ละ positive item (userID, itemID), สุ่ม negative items
        for itemID in pos_items:
            # สุ่มเลือก negative items ที่ไม่ได้มีการปฏิสัมพันธ์
            available_items = set(range(1, num_items + 1)) - pos_items
            negative_items = random.sample(available_items, 99)  # สุ่ม 99 negative items
            # สร้าง (userID, itemID) และตามด้วย 99 negative items
            negative_samples.append((userID, itemID, negative_items))
    return negative_samples

# ฟังก์ชันเขียน negative samples ลงในไฟล์ test.negative
def write_negative_samples(negative_samples, output_file):
    with open(output_file, "w") as f:
        for userID, itemID, neg_items in negative_samples:
            f.write(f"({userID},{itemID})\t" + "\t".join(map(str, neg_items)) + "\n")

# กำหนดเส้นทางไฟล์ (ปรับให้ตรงกับที่เก็บไฟล์จริงของคุณ)
input_file = "test.rating"  # ไฟล์ input test.rating
output_file = "test.negative"  # ไฟล์ output test.negative

# อ่านข้อมูลจาก test.rating
test_data = load_test_rating(input_file)

# สร้าง negative samples
negative_samples = create_negative_samples(test_data, num_items)

# เขียน negative samples ลงใน test.negative
write_negative_samples(negative_samples, output_file)

print(f"Number of negative samples generated: {len(negative_samples)}")
