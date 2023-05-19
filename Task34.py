stih = str(input("Введите стих Винни-Пуха: "))
glasnye = "аеёиоуыэюя"

counts = list()
count = 0

for item in stih.split():
    for i in item:
        if i in glasnye:
            count+=1
    counts.append(count)
    count = 0

print ("Парам пам-пам" if max(counts) == min(counts) else "Пам парам")