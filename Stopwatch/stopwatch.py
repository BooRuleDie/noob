import time
import os
import platform

'''
Color codes 

/033[STYLE;COLOR_CODE;BACKGROUND_CODEm

/033[0;0;0m:

Resets all color options but number of zeros are important here
For example if you want to used 2 options before like \033[2;31m you must write
\033[0;0m to reset.


COLOR_CODES: 

Black: 30
Red: 31
Green: 32
Yellow: 33
Blue: 34
Purple: 35
Cyan: 36
White: 37

BACKGRUND_CODES:

COLOR_CODES + 10

Example: \033[2;31m+\033[0;0m prints red plus sign '+'
'''

def print_sec_to_format(seconds):

    hours,minutes = 0,0
    
    while (seconds>=3600):
        hours+=1
        seconds-=3600
    while (seconds>=60 and seconds<3600):
        minutes+=1
        seconds-=60

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)

    h_m_s = f"{hours}:{minutes}:{seconds}"

    return h_m_s

def clear_screen(time_to_wait):
    
    time.sleep(time_to_wait)
    
    Current_OS = platform.platform()

    # It'also cross platform :D

    if "windows" in Current_OS.lower():
        os.system("cls")
    else: 
        os.system("clear")

def manualpage():

    manual_page = """\033[2;31m+\033[0;0m===============================================================\033[2;31m+\033[0;0m
|                         \033[2;37;41m MANUAL PAGE \033[0;0;0m                         |
\033[2;31m+---\033[0;0m=========================================================\033[2;31m---+\033[0;0m
|                                                               |
|  \033[32m 1 - Start: \033[0m                                                 |
|                                                               |
|  Starts the timer, you can only start the timer once.         |
|  If you try to enter "1" more than one time.                  |
|  Program gives you an error and takes you back to the options.|
|                                                               |
\033[2;31m+---\033[0;0m=========================================================\033[2;31m---+\033[0;0m
|                                                               |
|  \033[31m 2 - Stop: \033[0m                                                  |
|                                                               |
|  Stops the timer and prints respectively "Time passed since   |
|  last lap" and "Total Time Passed". After program printed     |
|  everything you can go to options by entering anyting.        |
|                                                               |
\033[2;31m+---\033[0;0m=========================================================\033[2;31m---+\033[0;0m
|                                                               |
|  \033[34m 3 - Write & Quit: \033[0;0m                                          |
|                                                               |
|  Creates a file in same directory with stopwatch6.py named    |
|  log.txt and logs all laps and "total time passed" since      |
|  start. Writes current date and time to the top left corner.  |
|  After first time, program appends log informations to file.  |
|                                                               |
|  Example:                                                     |
|                                                               |
|   +=======================+================+                  |
|   | Date: 06-04-2021      |                |                  |
|   | Time: 02:21:24        |                |                  |
|   +-----------------------+                |                  |
|   |                                        |                  |
|   | 1th lap: 00:00:01                      |                  |
|   | 2th lap: 00:00:06                      |                  |
|   | 3th lap: 00:00:01                      |                  |
|   |                                        |                  |
|   |Total time passed: 00:00:08             |                  |
|   +========================================+                  |
|                                                               |
\033[2;31m+---\033[0;0m=========================================================\033[2;31m---+\033[0;0m
|                                                               |
|  \033[2;30;41m4 - Quit:\033[0;0;0m                                                    |
|                                                               |
|  Quits without logging.                                       |
|                                                               |
\033[2;31m+\033[0;0m===============================================================\033[2;31m+\033[0;0m"""
    print(manual_page)

def banner():
    Banner = """  \033[2;31m______\033[0;0m                                         _     
 \033[2;31m/ _____) _\033[0;0m                             _       | |    
\033[2;31m( (____ _| |_ ___  ____\033[0;0m   _ _ _ _____ _| |_ ____| |__  
 \033[2;31m\____ (_   _) _ \|  _ \ \033[0;0m| | | (____ (_   _) ___)  _ \ 
 \033[2;31m_____) )| || |_| | |_| |\033[0;0m| | | / ___ | | |( (___| | | |
\033[2;31m(______/  \__)___/|  __/\033[0;0m  \___/\_____|  \__)____)_| |_|
                  \033[2;31m|_|\033[0;0m                
                                      \033[2;31mBy BooRuleDie\033[0;0m"""
    
    print(Banner)

def main():
    
    Real_Time_Passed = 0.0
    Real_Start = 0.0
    flag = 0
    records = []

    Table="""
    \033[2;31m+\033[0;0m------------------------\033[2;31m+\033[0;0m
    | \033[2;32m1 - Start\033[0;0m              | 
    | \033[2;31m2 - Stop\033[0;0m               |
    | \033[2;34m3 - Write & Quit\033[0;0m       |
    | 4 - Quit               |
    | 5 - Manual Page        |
    \033[2;31m+\033[0;0m------------------------\033[2;31m+\033[0;0m\n"""

    while(1):

        clear_screen(0)

        banner()
        print(Table)

        u_input = input("\033[2;33mPlease enter an operation number: \033[0;0m")

        if u_input ==  "1":
             
            if flag == False:
                
                Real_Start = time.time()
                
                print("\n\033[2;30;43m===========================================\033[0;0;0m\n\nStopwatch has started.\n\n\033[2;30;43m===========================================\033[0;0;0m")
                clear_screen(1)

                flag = True

            else:
                
                print("\n\033[2;30;43m===========================================\033[0;0;0m\n\nNot available now, It's started already.\n\n\033[2;30;43m===========================================\033[0;0;0m")
                clear_screen(1)
        
        elif u_input == "2":
            
            if flag==False:
                
                print("\n\033[2;30;43m===========================================\033[0;0;0m\n\nYou need to start timer first.\n\n\033[2;30;43m===========================================\033[0;0;0m")
                clear_screen(1)

            else:

                print("\n\033[2;30;43m===========================================\033[0;0;0m\n\nStopped.\n")
                
                stop =  time.time()
                Real_Time_Passed += int(stop-Real_Start)
                
                records.append(print_sec_to_format(int(stop-Real_Start)))

                for index,record in enumerate(records):
                    print(f"\033[2;31m{index+1}th lap is: \033[0;0m{record}")

                print(f"\n\033[2;32mPassed time since the beginning: \033[0;0m{print_sec_to_format(int(Real_Time_Passed))}.")
                con_input = input("\n\033[2;30;43m===========================================\033[0;0;0m\n\n\033[2;33mPress any number to start timer again: \033[0;0m")
                
                clear_screen(0)

                flag = True
                
                Real_Start = time.time()
            
        elif u_input == "3":
            
            if flag == False:
                
                print("\n\033[2;30;43m===========================================\033[0;0;0m\n\nThere is nothing to write.\n\n\033[2;30;43m===========================================\033[0;0;0m")
                clear_screen(1)
                
                continue

            stop = time.time()
            Real_Time_Passed += int(stop-Real_Start)
            
            records.append(print_sec_to_format(int(stop-Real_Start)))

            date = time.strftime("%m-%d-%Y")
            Time = time.strftime("%H:%M:%S")

            begin = f"+=======================+================+\n| Date: {date}\t|\t\t |\n| Time: {Time}\t|\t\t |\n+-----------------------+\t\t |\n|\t\t\t\t         |   \n"
            end = "+========================================+\n\n"

            with open("log.txt","a") as f:
                
                f.write(begin)
                
                for index,record in enumerate(records):
                    f.write(f"| {index+1}th lap: {record}\t\t\t |\n")
                
                f.write(f"|\t\t\t\t         |\n| Total time passed: {print_sec_to_format(int(Real_Time_Passed))}\t\t |\n")
                f.write(end)

            print("\n\033[2;30;43m===========================================\033[0;0;0m\n\nExiting...\n\n\033[2;30;43m===========================================\033[0;0;0m")
            clear_screen(1)
            
            break

        elif u_input  == "4":
            
            sure = input("\n\033[2;30;43m===========================================\033[0;0;0m\n\n\033[2;33mAre you sure? (y/n): \033[0;0m")

            if sure.lower() == 'y':
                
                clear_screen(0)
                
                break
            
            else:
                
                clear_screen(0)

        elif u_input == "5":
            
            clear_screen(0)
            
            manualpage()
            end_input = input("\n\033[2;33mEnter anything to quit: \033[0;0m")
            
            clear_screen(0)
        
        else:
            
            print(f'\n\033[2;30;43m===========================================\033[0;0;0m\n\n"{u_input}" is not a valid number.\n\n\033[2;30;43m===========================================\033[0;0;0m')
            clear_screen(1)
            
            continue
        
main()
