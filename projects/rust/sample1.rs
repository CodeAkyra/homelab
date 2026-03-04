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

macro_rules! named_arguments {
    () => {
        println!(
            "{layer1}, {layer2}, {layer3}, {layer4}, {layer5}, {layer6}, {layer7}",
            layer7 = "Application",
            layer6 = "Presentation",
            layer5 = "Session",
            layer4 = "Transport",
            layer3 = "Network",
            layer2 = "Data-Link",
            layer1 = "Physical",
        );
    };
}

macro_rules! positional_arguments {
    () => {
        println!("SPANNING TREE, TREE{}", "TREE!")
    };
}

fn main() {
    let num = 69420;
    //macro_rules, parang function()
    format_none!(num);
    format_bits!(num);
    format_octal!(num);
    format_hex!(num);

    // marco inside macro
    println!();
    format_none!(value!());
    format_bits!(value!());
    format_octal!(value!());
    format_hex!(value!());
    value!();

    println!();
    positional_arguments!();
    named_arguments!();
}
