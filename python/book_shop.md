Open the code challenge and analyze it.

1. Describe what the endpoint does.
2. There are some missing key pieces in this code example. Identify them.
   * Validate inputs (check if book_id, quantity and user_id are sent in the request).
   * Validate if quantity is a positive integer.
   * Check if book_id and user_id exist in the database. Handle exceptions with try-catch
   * Check if the book is in stock (i.e., quantity in database is higher than quantity provided by user).
   * Update book stock as well the user’s transaction history.
   * Bonus points:
     * Candidate mentions Authentication and Authorization
     * Locking the database when updating the stock to avoid concurrency issues.
     * Send email notification to user after purchase.