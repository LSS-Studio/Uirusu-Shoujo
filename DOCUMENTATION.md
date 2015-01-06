## Statements and Functions ##
In Uirusu Shoujo a small set of statements have been added to the Application Programming Interface (API) of the game, in order to aid the usage of basic functionality that is required by the storyline. The members of this set are described as follows:

### `points <name> <points> <date>` ###
The `points` statement is used by the game to change the opinion of a character towards the main character on a given day. The opinion of a character on a specific day will gradually deteriorate as the days progress throughout the game, and will be decremented by `1/365` every single day until `0` is reached after 365 days, after which the value of that opinion will continue to be null forever into the future. Some example usage could be:

`points ebby 20 2`*, the opinion of Ebola-chan towards the main character is '20' on the second day.*

`points joki -50 0`*, the opinion of Joki towards the main character is '-50' on the anteproximate day.*

`points sars 5 65`*, the opinion of Sars-chan towards the main character is '5' on the 65th day.*

### `day [set <day> | shift <amount> | end]` ###
The `day` statement is used to alter the current date in various ways. It consists of various unary *commands*, with associated arguments in the form of simple mathematical expressions. The command that is probably going to be used most commonly is the `end` command, which does nothing but increment the current date.

On top of that, there is the `set` command which sets the current date to a specific day. The `<day>` argument is in the form of a simple Ren'Py expression; ie. it can be not only equivalent to `((2 + 2) / 3)` but also utilise global functions and variables: `abs(amountOfCheese - 10)`. Do note the mandatory parentheses around expressions that contain multiple terms; ie. passing `day set 2 + 2` would be invalid, as the proper form is `day set (2 + 2)`, however `day set 4` is also valid as `4` is a single term.

The `shift` command is able to increment and decrement the current date by a specified amount. The argument is as with the `set` command likewise a simple Ren'Py expression. If the expression evaluates to a positive number, the current date will be incremented by that number; conversely, if the argument evaluates to a negative number, the current date will likewise be decremented by that amount.

### `