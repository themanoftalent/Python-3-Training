# # here we are going to define a list # #
# name = str(input("Enter your name : "))
#
# for i in range(len(name)):
#     print("Your name {}. letter: {}".format(i, name[i]))


website1 = "www.google.com"
website2 = "www.istihza.com"
website3 = "www.facebook.com"
website4 = "www.guru99.com"

for names in website1, website2, website3, website4:
    print("site: ", names[4:-4]) #dört karekter önden 4 karekter arkadan alınıp
    print("----------------------------------")
    #print("Önerilen site simleri ", names[:])
