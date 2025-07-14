def main():
    file_type = input("Enter File Name: ")
    file_type = file_type.casefold()

    if file_type.endswith(".jpeg") or file_type.endswith(".jpg"):
        print("image/jpeg")
    elif file_type.endswith(".zip"):
        print("application/zip")
    elif file_type.endswith(".txt"):
        print("text/plain")
    elif file_type.endswith(".gif"):
        print("image/gif")
    elif file_type.endswith(".pdf"):
        print("application/pdf")
    elif file_type.endswith(".png"):
        print("image/png")
    else:
        print("application/octet-stream")


main()
