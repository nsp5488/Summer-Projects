use bookbot::Book;

fn main() {
    let file_path = "books/frankenstein.txt";
    let book = Book::get_book_from_file(&file_path);
    book.print_report();
}  
