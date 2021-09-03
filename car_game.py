command = ""
started = False
stopped = False
while True:
        command  = input(">").lower()
        if command == "start":
            if started == True:
                print("Car already started")
            else:
                print("car started . . .")
                started = True
        elif command == "stop":
            if not started:
                print("Car is already stopped. You need to start it")
            else:
                started = False
                print("Car stopped")
                stopped = True
        elif command == "help":
            print("""
start - to start the car
stop - to stop the car
quit - to quit
            """)
        elif command =="quit":
            if not started and not stopped:
                print("The car has been off.")
            
            elif stopped:
                print("godbye")
                started = False
             
        else:
            print("I can't understand that")
   else:
        print("Type 'help' for instruction")

