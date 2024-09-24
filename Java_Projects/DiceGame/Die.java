package DiceGame;

import java.util.Random;
import java.util.Scanner;

public class Die {
    private int currentValue;
    private int maxDiceValue;
    private Random rand = new Random();

    Die(int maxDiceValue) { // constructor.
        this.maxDiceValue = maxDiceValue;
    }

    public void roll() { // Rolls dice method. 1-6. When called updates currentvalue variable to a new random value.
        this.currentValue = rand.nextInt(this.maxDiceValue) + 1;
    }

    public int getCurrentValue() { // returns current value of dice when called. e.g. result of .roll()
        return currentValue;
    }

}

class Player {
    private String name;
    private int points = 0;
    private Die dice; // Die type, dice variable name. 

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
        System.out.println("You roll the dice!");
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

    public static String slowPrint(String s) throws InterruptedException { //print strings slowly
        char[] chars = s.toCharArray();

        for (int i = 0; i < chars.length; i++) {
            System.out.print(chars[i]);
            Thread.sleep(30);
        }
        return s;
    }

    public static void main(String[] args) throws InterruptedException {

        Scanner sc = new Scanner(System.in);
        int maxRounds, rounds = 0; // declare variables for max rounds and round counter.
        slowPrint("Hello, welcome to DiceGame\nHow many rounds would you like to play?\n");
        maxRounds = sc.nextInt();
        sc.nextLine(); //consumes next nextline, so we can ask 

 
        slowPrint("Enter your name: ");
        Player player1 = new Player(sc.nextLine()); //creates player putting user input as name.
        player1.addDie(); //creates new dice instance for player1 instance of player class.

        while (rounds < maxRounds) { 
            rounds++; //round started, add 1 to round counter.
            slowPrint("\nPlease guess a number 1-6: ");
            int usrGuess = sc.nextInt();// player guess = scanner object

            player1.rollDice(); //future update, add a 2nd guess. and the program will tell you under or over.
            
            if (usrGuess == player1.getDieValue()) {// check if player usrGuess == dice.currentValue
                player1.increaseScore(); // if yes increaseScore method called.
                System.out.println("Hurray! You guessed correctly!\nYour current score is: " + player1.getPoint());
            } else {
                slowPrint("You guessed wrong!\nThe correct number was: ");
                System.out.print(player1.getDieValue());
            }
            
        }
        
        System.out.println("\nGame over, Thanks for playing " + player1.getName() + "\nYour final score is: " + player1.getPoint());
        
        sc.close();
    }
}
