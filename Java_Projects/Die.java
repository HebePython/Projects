import java.util.Random;
import java.util.Scanner;

public class Die {
    int currentValue;
    int maxDiceValue;
    private Random rand = new Random();

    Die(int maxDiceValue) { // constructor.
        this.maxDiceValue = maxDiceValue;
    }

    public void roll() { // Rolls dice method. 1-6. When called updates currentvalue variable to a new random value.
        this.currentValue = rand.nextInt(this.maxDiceValue) + 1;
    }

    public int getCurrentValue() { // returns current value of dice roll when called.
        return currentValue;
    }

}

class Player {
    String name;
    int points = 0;
    Die dice; // Die type, dice variable name. 

    Player(String name) { //constructor, takes only name.
        this.name = name;
    }

    public String getName() { // returns name of player when called.
        return name;
    }

    public int getPoint() { //getter points. returns current amount of points when called.
        return points;
    }

    public void rollDice() { // rolls dice, dice is of Die type so it has .roll() method.
        dice.roll();
        System.out.println("You roll the dice and get: " + getDieValue());
    }

    public int getDieValue(){ //returns value of dice roll
        return dice.getCurrentValue(); // get current value
    }

    public void increaseScore() { //increases player score when called.
        this.points++;
    }

    public void addDie() { //creates new die for player and adds max dice value.
        this.dice = new Die(6); 
    }
}

class DiceGame { // main game 

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int maxRounds, rounds = 0; // declare variables for max rounds and round counter.
        System.out.println("Hello, welcome to DiceGame\nHow many rounds would you like to play? ");
        maxRounds = sc.nextInt();
        sc.nextLine(); //consumes next nextline, so we can ask 

        // Ask for player name, create new player object.
        System.out.println("Enter your name: ");
        Player player1 = new Player(sc.nextLine()); //creates player putting user input as name.
        player1.addDie(); //creates new dice object, 

        while (rounds < maxRounds) { 
            rounds++; //round started, add 1 to round counter.
            System.out.println("Please guess a number 1-6: ");
            int usrGuess = sc.nextInt();// player guess = scanner object

            player1.rollDice(); //future update, add a 2nd guess. and the program will tell you under or over.
            
            if (usrGuess == player1.getDieValue()) {// check if player usrGuess == dice.currentValue
                player1.increaseScore(); // if yes increaseScore method called.
                System.out.println("Hurray! You guessed correctly!\nYour current score is: " + player1.getPoint());
            } else {
                System.out.println("You guessed wrong!\nThe correct number was: " + player1.getDieValue());
            }
            
        }
        
        System.out.println("Game over, Thanks for playing " + player1.getName() + "\nYour score was: " + player1.getPoint());
        
        sc.close();
    }
}
