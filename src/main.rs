fn main() {
    println!("Hello from Rust!");

    let a: i32 = 5;
    let b: i32 = 7;
    println!("{} + {} = {}", a, b, add(a, b));
}

fn add(x: i32, y: i32) -> i32 {
    x + y
}
