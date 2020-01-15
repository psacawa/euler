use std::collections::HashSet;

const LIMIT_N : u64 = 10_000;

fn p(n: u32) -> u64 {
   let p = (n*(3*n-1)/2)  as u64;
   p
}

fn main() {
    let mut pentagonal = HashSet::<u64>::new ();
    for i in 1..LIMIT_N {
        pentagonal.insert (p (i as u32));
    }
    // println! ("{:?}", pentagonal)
    for j in pentagonal.iter () {
        for k in pentagonal.iter () {
            if k > j{
                let sum = j+k;
                let diff = k-j;
                if pentagonal.contains (&sum) && pentagonal.contains (&diff){
                    println! ("{} {} diff={}", j, k, k-j)
                }
            }
        }
    }


}
