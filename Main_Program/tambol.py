with open("tambol.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

with open("tambol_deta.txt", "w", encoding="utf-8") as output_file:
    for line in lines:
        if "VALUES" in line:
            # ตัดส่วน VALUES ออก
            values_part = line.split("VALUES")[1]

            # ลบเครื่องหมายวงเล็บ, ช่องว่าง, และ ;
            values_part = values_part.strip(" ();\n").replace("'", "")

            # แยกค่าด้วยเครื่องหมายคอมมา
            values = values_part.split(", ")

            # จัดรูปแบบผลลัพธ์
            mcode = values[0]
            mname = values[1]
            
            # สร้างสตริงผลลัพธ์ตามที่ต้องการ
            output = f"{mcode} {mname}\n"

            # เขียนข้อมูลลงไฟล์ text
            output_file.write(output)

print("done")