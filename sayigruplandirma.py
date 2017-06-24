import random
#random mudülünü import ederek bilgisayarın rastgele bir sayı oluşturması için gerekli fonksiyonları kullanabiliyorum.
def fonk():
    #random.sample kullanarak rastgele sayılar atıyorum 0,20 ile hangi aralıkta seçeceğimi ve 10 ile kaç tane sayı seçeceğini yazıyorum.
    a = random.sample(range(0,21),10)
    b = random.sample(range(0,21),10)
    c = []
    d = []
    print(a)
    print(b)
    #i a nın içinde ve i b nin içindeyse o sayıyı c listesine at diyorum
    for i in a:
        if i in b:
            c.append(i)
    #i a nın içinde ce b nin içinde değilse o sayıyı d listesine at diyorum        
        else:
            d.append(i)
    # i b nin içinde ve a nın içinde değilse d listesine at diyorum bunu iki kere yapmamın nedeni kesişim kümesi dışındaki her elemanı almak istediğimden
    for i in b:
        if i not in a:
            d.append(i)
    print(c)
    print(d)
fonk()
