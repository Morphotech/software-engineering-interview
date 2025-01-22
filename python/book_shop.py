def purchase_book(request):
    # Parse inputs from request
    data = request.json
    book_id = data['book_id']
    quantity = data['quantity']
    user_id = data['user_id']

    user = get_user(user_id)
    book = get_book(book_id)

    pay(book.price * quantity, user)

    return {'message': 'Book purchased successfully!', 'code': 201}


def get_book(book_id):
    # Assume this method returns a book object corresponding to its book_id
    pass


def get_user(user_id):
    # Assume this method returns a user object corresponding to its user_id
    pass


def pay(amount, user):
    # Assume this method processes the payment for the user
    pass
