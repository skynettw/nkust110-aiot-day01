with open("data.csv", "r", encoding="UTF-8") as fp:
    data = fp.readlines()

for line in data[1:]:
    name, h, w = line.split(",")
    h = int(h)
    w = int(w.strip())
    bmi = round(w / ((h/100)**2), 2)
    print("{}的身高是{}公分，體重是{}公斤，BMI是{}".format(
        name, h, w, bmi))