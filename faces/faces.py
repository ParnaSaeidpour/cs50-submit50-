def main():

    message = convert(input())
    print(message)
    


def convert(message):
    new_message1=message.replace(":)",'🙂')
    new_message2=new_message1.replace(":(",'🙁')

    return new_message2


main()
