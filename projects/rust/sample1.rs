// macro_rules! command {
//    () => {
//        format!("Hello!")
//    };
// }

macro_rules! format_none {
    ($none:expr) => {
        println!("Normal: {}", $none)
    };
}

macro_rules! format_bits {
    ($bit:expr) => {
        println!("Bits: {:b}", $bit)
    };
}

macro_rules! format_octal {
    ($octal:expr) => {
        println!("Octal: {:o}", $octal)
    };
}

macro_rules! format_hex {
    ($hex:expr) => {
        println!("Hexadecimal: {:x}", $hex)
    };
}

macro_rules! value {
    () => {
        10
    };
}

fn main() {
    let num = 69420;

    format_none!(num);
    format_bits!(num);
    format_octal!(num);
    format_hex!(num);

    format_none!(value!());
    format_bits!(value!());
    format_octal!(value!());
    format_hex!(value!());
    value!();
}
