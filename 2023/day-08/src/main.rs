use std::fs;
use std::collections::HashMap;
use regex::Regex;

fn is_finished(currents: &Vec<String>) -> bool {
    for current in currents {
        if current.chars().nth(2).unwrap() != 'Z' { return false; }
    }
    return true;
}

fn main() {
    let contents = fs::read_to_string("ressources/data.txt")
        .expect("Something went wrong reading the file");

    let lines = contents.split("\n").collect::<Vec<&str>>();

    let mut instructions = lines[0].chars().into_iter().cycle();

    let re = Regex::new(r"(...) = \((...), (...)\)").unwrap();

    let mut currents = Vec::new();

    let dict = lines[2..].into_iter().fold(HashMap::new(), |mut acc, line| {
        if line.len() == 0 { return acc; }
        let caps = re.captures(line).unwrap();
        let key = caps.get(1).unwrap().as_str().to_string();

        if key.chars().nth(2).unwrap() == 'A' { currents.push(key.clone()); }

        let value1 = caps.get(2).unwrap().as_str().to_string();
        let value2 = caps.get(3).unwrap().as_str().to_string();

        acc.insert(key, (value1, value2));
        return acc;
    });

    let mut iterations = 0;

    while !is_finished(&currents) {
        if instructions.next().unwrap() == 'L' {
            currents = currents.iter()
                .map(|current| dict.get(current).unwrap().0.clone()).collect();
        } else {
            currents = currents.iter()
                .map(|current| dict.get(current).unwrap().1.clone()).collect();
        }
        iterations += 1;
        if iterations >= 100000000 { break; }
    }

    println!("Iterations: {}", iterations);
}
