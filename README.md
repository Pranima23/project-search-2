# project-search-2
Things accomplished:
1. Menu page dynamically displays items stored in database.
     Template->

2. Database created with minimal requirements. For this, following models are created: 
    Customer
 For storing data from restaurant site:
    Item
    Event
    Table
 For storing data from customer side:
    For Reservation
      Reservation
      
    For placing order
      Order
      OrderDetails
      
    For booking event
      (Thinking to create a newtable called BookEvent)
    
3. Made separate apps: Registration for Customers account, Events for handling events and Reservation for handling reservations, Items(already existing) for handling orders

    Also, kept related models (already created and messed up in items app)in the related apps

4. signup, login and logout added
left: reset password feature in login, invalid entry message at invalid entry

5. some functions related to cart