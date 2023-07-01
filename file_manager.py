def data_input():
    with open("INPUT.txt", "r") as fp:
        word = fp.readline().rstrip('\n')
        return word

def data_output(result):
    with open("OUTPUT.txt", "a+") as fp:
        if result:
            fp.write("ACCEPT\n")
        else:
            fp.write("REJECT\n")