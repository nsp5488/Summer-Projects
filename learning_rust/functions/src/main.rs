use std::io;


fn main() {
    println!("Hello, world!");

    another_func(2);
    let x = 5;
    let y = 4;

    println!("{x} + {y} = {}",add(x,y));

    let n:usize = 75;
    println!("The {n}th fibonacci number is {}", fib(n));

    let f = 40;
    let c = 15;

    println!("{f} in farenheit is {} in celsius", farenheit_to_celsius(f));
    println!("{c} in celsius is {} in farenheit", celsius_to_farenheit(c)); 

    println!("Enter a number to get the fib of that number: ");
    let mut fib_num = String::new();
    io::stdin()
        .read_line(&mut fib_num)
        .expect("Enter a number!");

    let fib_num : u32 = fib_num.trim().parse().expect("Enter a valid positive number");

    println!("The fib of {fib_num} is {}", recursive_fib(fib_num));

}

// Random function prints x
fn another_func(x:u8) {
    println!("Another function. Passed value {x}");
}

// Adds two i32s
fn add(x:i32, y:i32) -> i32 {
    x + y
}


// Computes the nth fibonacci number
fn fib(n: usize) -> u64 {
    let mut f = [0;256];
    f[0] = 0;
    f[1] = 1;
    let mut c = 2;
    while c <= n {
        f[c] = f[c-1] + f[c-2];
        c += 1;
    }
    f[n]
} 

fn recursive_fib(n:u32) -> i32 {
    if n == 0 {
        return 0;
    }
    if n == 1 {
        return 1;
    }
    return recursive_fib(n-1) + recursive_fib(n-2);
}

// Converts Farenheit to celsius
fn farenheit_to_celsius(f:i32) -> f32 {
    let f : f32 = f as f32;
    (f-32.0) * (5.0/9.0) 
}

// Converts celsius to farenheit
fn celsius_to_farenheit(c:i32) -> f32 {
    let c : f32 = c as f32;
    (c * (9.0/5.0)) + 32.0
}