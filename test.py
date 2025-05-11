from scipy.stats import shapiro 

male_sleep = [8,7,9, 6, 6,6,5, 6,8,8,7, 4,4,5,5,7]
W,pval = shapiro(male_sleep)

print(f"W: {W}")
print(f"p-val: {pval}")

if (pval > 0.05):
    print("Data appears to be normally distributed")
else:
    print("Data doesn't appear to be normally distributed")

