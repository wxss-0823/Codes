mod lifetime;
mod macros;

fn main() {
    // lifetime::str_life_time();
    let my_vec: Vec<i32> = vec![1,2,3];
    println!("{:?}", my_vec);
}
