# this function uses global variable s
def f():
    s="i live in khorram abad"
    print(s)

# main
s = "i live in iran"
f()
print(s)


"""متغیر s درون تابع f محلی است و روی متغیر جهانی s تاثیری ندارد به همین دلیل 
وقتی که print(s) در سطح بالا اجرا میشود مقدار آن هنوز i live in iran باقی مانده است."""