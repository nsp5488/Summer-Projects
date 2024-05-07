#[derive(Debug)]
struct Rectangle {
    width : u32,
    height : u32,
}
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    
    fn can_hold(&self, other:&Rectangle) -> bool {
        self.width >= other.width && self.height > other.height
    }

    fn square(size : u32) -> Self {
        Rectangle {
            width : size,
            height : size,
        }
    }
}

fn main() {
    let rect = Rectangle {
        width : 30,
        height : 50
    };

    let rect2 = Rectangle {
        width : 10,
        height : 40
    };
    let rect3 = Rectangle {
        width : 60,
        height : 45
    };


    println!("The area of the rectangle is {}", rect.area());
    println!("The rectangle is {:#?}", rect);

    println!("Can rect1 hold rect2? {}", rect.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect.can_hold(&rect3));

    let sq = Rectangle::square(15);

    println!("The area of the square is {}", sq.area());

}