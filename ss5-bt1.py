# nguyên nhân dẫn đến sai là gán nhầm biến

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

result = ""

for month in range(1, month_count + 1):
    for branch in range(1, branch_count + 1):
        revenue = int(
            input(f"Nhập doanh thu Chi nhánh {month}, tháng {branch}: ")
        )

        result = result + f"Chi nhánh {month}, tháng {branch}: {revenue} triệu đồng\n"

print(result)