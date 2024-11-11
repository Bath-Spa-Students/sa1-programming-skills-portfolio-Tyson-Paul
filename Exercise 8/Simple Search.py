def search():
    #List of string(names)
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
    
    #To ask the user to input the search term
    search_term = input("Enter the name you want to search for: ")
    
    if search_term:
        target_name = "Sam"
    
    #To display the result
    result = search_name(names, search_term)
    print(result)


def search_name(names_list, search_term):
    #To check if the search term is present in the list of names
    if search_term in names_list:
        return f"'{search_term}' found in the list."
    else:
        return f"'{search_term}' not found in the list."
    
# Run the program
if __name__ == "__main__":

 search()