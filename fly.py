import InsectClass as i

def main():
       fly = i.Insect(2,4)
       mosq = i.Insect(4,4)

       fly.randistance()
       mosq.randistance()

       print("The fly was able to fly", fly.get_distance(), "miles")
       print("the mosquito was able to fly", mosq.get_distance(),"miles")


       

# Call the main function.
main()
