macro_rules! say_hello {
    () => {
        println!("Hello Another World!")
    };
}

macro_rules! hello_name {
    ($name:expr) => {
        println!("Hello! {}!", $name)
    };
}

fn main() {
    println!("Hello World!");

    say_hello!();

    name!();

    let user = "Mark";

    hello_name!(user);

    let x = 5 + /* 90 + */ 5;
    println!("Is 'x' 10 or 100? x = {}", x);
}
