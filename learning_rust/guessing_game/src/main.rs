use std::io;
use std::cmp::Ordering;
use rand::Rng;


fn main() {
    println!("Guess the number!");

    // Gen random number
    let secret = rand::thread_rng()
    .gen_range(1..=100);

    // While we haven't guessed the number
    loop {

        // Get the guess as a string
        let mut guess = String::new();
        println!("Enter your guess: ");
        io::stdin()
                .read_line(&mut guess)
                .expect("failed to read line!");

        // Attempt to parse the guess into an int
        let guess : u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        // Print the guess
        println!("You entered {guess}");

        // Print too small/too large/correct
        match guess.cmp(&secret) {
            Ordering::Less => println!("Too small"),
            Ordering::Equal => {
                println!("Correct!");
                break;},
            Ordering::Greater => println!("Too big!")
        }
    }
}
