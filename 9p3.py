def f():
    global s
    s='i live in khorram abad.'
    print(s)

# main: Global Scope
s = 'i live in iran.'
f()
print(s)


"""این کد نحوه استفاده از متغیر گلوبال را نمایش میدهد که با استفاده از آن به تابع f اجازه 
میدهیم که به متغیر s در سطح جهانی دسترسی داشته باشد و آنرا تغییر دهد . اگر متغیر گلوبال را
نداشتیم تابع f فقط میتوانست یک متغیر محلی به نام s تعریف کند که با متغیر جهانی تداخل پیدا 
میکرد و تغییر نمی یافت"""