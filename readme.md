                                                    PIZZAA API
Overview:
I have to create a Django application which should be able to store information about different types of Pizza, then create an API interface that lists the information about all the different stored pizzas, and also be able to interact with that information (such as edit or delete).

Technology Used:
Python , Django Framework , Postgresql
Software used:
Postman Api (for testing the API) , 
Visual Studio Code (IDE)
PGADMIN 4

API ENDPOINTS:

1. http://127.0.0.1:8000/apimaster/api/createPizza

This endpoint is dedicated for creating a pizza, by adding the details, of the pizza topping , pizza size and pizza type.

HOW TO CHECK:
run the server -> go to postman -> click on POST-> add the http://127.0.0.1:8000/apimaster/api/createPizza.
-> BODY:


{
    "typeOfPizza":" Regular",
    "sizeOfPizza":"small",
    "toppingOfPizza":"Onion,jalapeno"
}

click the send button
it will push this data into the database.

2. http://127.0.0.1:8000/apimaster/api/listPizza

This endpoint is dedicated for API which lists the information about all the stored pizza, the response of this should also contain the information about the toppings, size and type of Pizza.

HOW TO CHECK:
run the server -> go to postman -> click on GET-> add the http://127.0.0.1:8000/apimaster/api/listPizza
click the send button
By this you will GET all the pizza stored in the database.


3. Filtering the Pizza based on size and type:
        3.1 filtering of pizza based on size:
            http://127.0.0.1:8000/apimaster/api/filterBySize/large
            HOW TO CHECK:
            run the server -> go to postman -> click on GET-> add the http://127.0.0.1:8000/apimaster/api/filterBySize/large
            click the send button

        3.2 filtering of pizza based on type:
            http://127.0.0.1:8000/apimaster/api/filterByType/Square
            HOW TO CHECK:
            run the server -> go to postman -> click on GET-> add the http://127.0.0.1:8000/apimaster/api/filterByType/Sqaure
            click the send button

4. Edit/update a pizza
http://127.0.0.1:8000/apimaster/api/updatePizza/2

HOW TO CHECK:
run the server -> go to postman -> click on PUT-> add the http://127.0.0.1:8000/apimaster/api/updatePizza/2
click the send button

5. Deleting A pizzaa
http://127.0.0.1:8000/apimaster/api/deletePizza/1

HOW TO CHECK:
run the server -> go to postman -> click on DELETE-> add the http://127.0.0.1:8000/apimaster/api/deletePizza/2
click the send button




STEPS TO RUN THE PROJECT:


1. Download this repository in your local computer
2 . In the repository open the command prompt
3. In the command prompt type:

pip install -m venv env

4. activate your environment by typing:
env\Scripts\activate.bat
5. 
pip install install -r requirements.txt

6. python manage.py runserver





