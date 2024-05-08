use std::collections::HashMap;

fn main() {
    vectors();
    strings();
    hashmaps();
}

fn hashmaps() {
    let mut nums:Vec<i32> = vec![6, 8, 2, 4, 1, 2];
    nums.sort();
    let median = nums.get(nums.len() / 2).unwrap_or(&0);

    let mut total = 0;
    let mut map: HashMap<i32, i32> = HashMap::new();

    for num in &nums {
        total += num;
        let count = map.entry(*num).or_insert(1);
        *count += 1
    }
    let mean:f64 = total as f64 / nums.len() as f64;

    let mut max = -1;
    let mut max_key = 0;
    for (key, value) in &map {
        if *value > max {
            max = *value;
            max_key = *key;
        }
    }

    println!("Nums has mean: {mean}, median: {median}, and mode: {max_key}");


}

fn strings() {
    let _s = String::new();

    let mut s1 = String::from("foo");
    let s2 = "bar";
    s1.push_str(s2);
    println!("s2 is {s2}");
    let mut s = String::from("lo");
    s.push('l');


    let vowels = vec!['a', 'e', 'i', 'o', 'u'];

    let input_str = String::from("Apple");
    let mut iterator = input_str.chars();
    let first = iterator.next().unwrap();

    if vowels.contains(&first.to_ascii_lowercase()) {
        println!("{}-hay", input_str);
    } else {
        let remaining: String = iterator.take(input_str.len() - 1).collect();

        println!{"{}-{}ay", &remaining, first};
    }
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