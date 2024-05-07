fn main() {
    // vectors();
    strings();
}

fn strings() {
    let mut s = String::new();
    let data = "initial contents";

    let s = data.to_string();

    // the method also works on a literal directly:
    let s = "initial contents".to_string();
    let s = String::from("initial contents");
    let mut s1 = String::from("foo");
    let s2 = "bar";
    s1.push_str(s2);
    println!("s2 is {s2}");
    let mut s = String::from("lo");
    s.push('l');
}

fn vectors() {
    let mut v : Vec<i32> = Vec::new();
    v.push(0);
    v.push(1);


    println!("The 0th index is holding {}", &v[0]);
    v.push(2);

    let first = v.get(1);

    if let Some(first) = first {
        println!("The 1st index is holding {}", first);
    } else {
        println!("There is no value in the 1st index!");
    }
    
    let mut v2 = vec![1,2,3,4,5];

    for i in &v2 {
        println!("Before mutation: {i}");
    }
    for i in &mut v2 {
        *i *= 2;
    }

    for i in &v2 {
        println!("After mutation: {i}");
    }  
}