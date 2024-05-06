fn main() {
    println!("Hello, world!");

    another_func(2);
    let x = 5;
    let y = 4;

    println!("{x} + {y} = {}",add(x,y));

    let n:usize = 6;
    println!("The {n}th fibonacci number is {}", fib(n));

    let f = 40;
    let c = 15;

    println!("{f} in farenheit is {} in celsius", farenheit_to_celsius(f));
    println!("{c} in celsius iin {} in farenheit", celsius_to_farenheit(c)); 
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
fn fib(n: usize) -> i32 {
    let mut f = [0;7];
    f[0] = 0;
    f[1] = 1;
    let mut c = 2;
    while c <= n {
        f[c] = f[c-1] + f[c-2];
        c += 1;
    }
    f[n]
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