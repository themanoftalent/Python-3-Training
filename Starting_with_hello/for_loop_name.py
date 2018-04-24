# # here we are going to define a list # #
# name = str(input("Enter your name : "))
#
# for i in range(len(name)):
#     print("Your name {}. letter: {}".format(i, name[i]))


site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

for isim in site1, site2, site3, site4:
    print("site: ", isim[4:-4]) #dört karekter önden 4 karekter arkadan alınıp
    print("----------------------------------")
    print("Önerilen site simleri ", isim[:])
