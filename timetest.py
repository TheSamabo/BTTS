import time



while(True):
    now_min = time.gmtime()[4]
    now_sec= time.gmtime()[5]

    # print(now_sec)
    if str(now_min)[0] == "0":
        lig = str(now_min)[1]
        
    else:
        lig = str(now_min)[0]


    if lig == "3" or lig == "6" or lig == "9":
        if str(now_sec) == "1":
            #code

# while(True):
#     print(now_sec)
