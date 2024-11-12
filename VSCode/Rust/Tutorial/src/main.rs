mod lifetime;

fn main() {
    // lifetime::str_life_time();
    let array = [2u8; 5];
    for num in array {
        print!("{}, ", num)
    }
}
