import InsectClass as i


# The main function.
def main():
       # Create an object from the Coin class.
       fly = i.Insect()   # this creates an instance called 'my_coin' of the class 'Coin()'
       fly.randistance()
       print("The fly was able to fly", fly.get_distance(), "miles")
       
       mosq = i.Insect()
       mosq.randistance()
       print("the mosquito was able to fly", mosq.get_distance(),"miles")
           


       

# Call the main function.

main()
