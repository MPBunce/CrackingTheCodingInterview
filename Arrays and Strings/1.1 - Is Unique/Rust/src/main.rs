#![allow(non_snake_case)]

fn main() {
    let testString = String::from("apples");

    if isStringUniqueTwoLoops(&testString) {
        println!("{}, - Two Loop Method - This is a unique string!\n", &testString)
    } else {
        println!("{}, - Two Loop Method - This is not a unique string :(\n", &testString)
    }

    if isStringUniqueHashMap(&testString) {
        println!("{}, - Hashmap Method - This is a unique string!\n", &testString)
    } else {
        println!("{}, - Hashmap Method - This is not a unique string :(\n", &testString)
    }

}

fn isStringUniqueTwoLoops(msg: &String) -> bool{

    //Cannot iterate over a string in Rust convert to char vector XD
    let my_vec: Vec<char> = msg.chars().collect();
    println!("THE STRING : {}", msg);

    for i in 0..my_vec.len() {
        for j in i..my_vec.len() {

            if my_vec[i] == my_vec[j] {
                return false;
            }

        }
    }

    return true;
}

fn isStringUniqueHashMap(msg: &String) -> bool{
    println!("THE STRING : {}", msg);
    return true;
}