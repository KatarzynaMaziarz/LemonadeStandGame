Description of Game:

The lemonade game starts by calling a function asking if the user wants to play.
A loop keeps this question active until the user provides valid input. 
If the input is "n", the game exits.
If the answer is "y", the game prints a message and prompts the user to hit enter to continue. 
It then enters the main loop which will run until the user quits the game.
Then the game calls a function that prints the rules.

The game calculates the forecast for the next day along with the cost to make lemonade, 
and calls a function that displays the forecast for the user.
Then the game calls a function that displays the list of choices for the user. 
The menu prompts the user to input their action and loops until the user provides a valid choice.
Once a valid choice is made, the program enters another loop that will continue until the user chooses to sell lemonade 
or chooses option 3 to close for the day.
If the user chooses 4, the program calls the forecast function and redisplays the forecast.
If they choose 5, it calls the rules function and redisplays the rules.
If they choose 6, the program displays a message and quits.

If the user chooses 3, close for the day, the secondary loop breaks 
and the main loop runs advancing to the next day with a new forecast and a new price to make lemonade.

If the user chooses 2, the program calls a function to make lemonade. The price of lemonade is displayed.
The user chooses how many cups of lemonade to make and the number of cups is added to inventory. 
The cost to make the cups is deducted from the cash the user has and the menu redisplays.

If the user chooses 1, the program calls the sell lemonade function. 
The function prompts the user for a price with a maximum of $1 (100 cents).
It enters a loop where it will not proceed until the user enters a valid price. 
After the user enters a avalid price, the function calculates the cups sold and displays a message to the user based on the outcome.
Any profit is added to cash. The day advances and the main loop restarts.

When the user quits the application, a different message is displayed depending on whether they made a profit, broke even or lost money.



