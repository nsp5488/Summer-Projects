use std::fs;
use std::collections::HashMap;
use std::cmp::Ordering;

pub struct Book {
    word_count: u64,
    char_counts: Vec<CharCount>
}

impl Book {
    pub fn get_book_from_file(file_path: &str) -> Book {
        let contents = fs::read_to_string(file_path).expect("Should have been readable");
        Book::new(contents)
    }

    pub fn new(contents : String) -> Book{
        let mut wc = 0;
        for line in contents.lines() {
            for _ in line.split(" ") {
                wc += 1;
            }
        }
    
        Book {
            word_count: wc,
            char_counts: Self::get_character_counts(contents)
        }
    }

    pub fn print_report(self) {
        println!("Printing Report!");
        println!("There were a total of {} words found in the book", self.word_count);
        for char_count in self.char_counts {
            println!("{} occurred {} times", char_count.character, char_count.count);
        }
        println!("Report complete!")

    }
    fn get_character_counts(contents: String) -> Vec<CharCount> {
        let mut characters: HashMap<char, u64> = HashMap::new();
        for line in contents.lines() {
            for ch in line.chars() {
                if ch.is_alphabetic() {
                    let count = characters.entry(ch).or_insert(0);
                    *count += 1;
                }
            }
        }

    let mut sorted = Vec::new();
    for (key, value) in characters {
        sorted.push(CharCount::new(key, value));
    }
    sorted.sort_by(|a,b| b.cmp(a));
    sorted

    }

}
#[derive(Eq)]
struct CharCount {
    character : char,
    count : u64
}


impl CharCount {
    pub fn new(character :char, count : u64) -> CharCount {
        CharCount {
            character, 
            count
        }
    }
}
impl Ord for CharCount {
    fn cmp(&self, other: &Self) -> Ordering {
        self.count.cmp(&other.count)
    }
}

impl PartialOrd for CharCount {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for CharCount {
    fn eq(&self, other:&Self) -> bool {
        self.count == other.count
    }
}






#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn build_book() {
        let s = String::from("one two three");
        let b = Book::new(s);
        assert_eq!(3, b.word_count);
        assert_eq!("one two three", b.full_text);
    }

    #[test]
    fn get_characters() {
        let s = String::from("abc\ndef");
        let b = Book::new(s);

        for char_count in b.get_character_counts() {
            if "abc\ndef".contains(char_count.character) {
                assert_eq!(1, char_count.count);
            }
        }
    }
}