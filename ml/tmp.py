from ml.dataPrep import predictor, le

a, b = predictor(3000000, 9.6, 0.2, 16)
print(float(le.inverse_transform([int(a[0])])[0]), "+-", b)
