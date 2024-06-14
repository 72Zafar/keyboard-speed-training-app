from time import *
import random as rd

def mistake(partest , usertest):
    erorr = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i] :
                erorr = erorr + 1
        except:
            erorr = erorr + 1
    return erorr         


def speed_time (s_time , e_time ,userinput):
    time_delay = e_time - s_time
    time_r = round(time_delay,2)
    speed = len(userinput)/ time_r
    return round (speed)


if __name__ == "__main__":
    while True:
        user = input("Ready to test : yes / no :")
        if user == "yes":

           test = ["python langange is good ", "my name is zafar","i am learning  the Data science","and machine learning","wellcome to  my programme "]

           test_random = rd.choice(test)

           print ("# Typing Speed #")

           print (test_random)

           time_1 = time()
           test_input = input("Enter: ")
           time_2 = time()


           print ("Speed: ", speed_time (time_1 , time_2 ,test_input),"w/sec")
           print ("Erorr: ",mistake(test_random,test_input))

        elif user == "no":
            print ("Thank You")
            break
        else:
            print ("Wrong input")

      