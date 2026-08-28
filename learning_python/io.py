#with open("practice.text","w") as f:
 #   f.write("Hi everyone\ni am learning fileI/O\n")
  #  f.write("using python.")
 
def check_for_line():
    word = "python"
    data = True
    line_no = 1
    with open("practice.text","r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no +=1

    return -1
check_for_line()
