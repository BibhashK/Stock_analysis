import webbrowser
import time

total_break = 10
break_count = 0
print("the program has started!")
while(break_count <total_break):
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=tAWwoElTPXo")
    break_count += 1