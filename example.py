# Get the comment of the parrent
def parent(grade):
    """parent command function

    Args:
        grade: student's grade.
    """
    if grade < 5:
        print("You're adopted")
    elif grade < 10:
        print("What a dumb kid")
    elif grade < 15:
        print("Noice")
    elif grade < 20:
        print("Why not 20 ?")
    else:
        print("Why not 21 ?")

# Main function
def main():
    """This is the main function"""
    grade = input("Give me your grade: ")
    try:
        grade = int(grade)
        parent(grade)
    except ValueError as e:
        print("ValueError : ", e)
    finally:
        print("THE END !")

if __name__ == "__main__":
    main()