fn main() {
    let a = vec!["println!(\"let a = vec!\", a)", "println!(\"fn main() {{\");\n    println!(\"    let a = vec!{:?};\", a);\n    println!(\"    {}\", a[1]);\n    println!(\"}}\");"];
    println!("fn main() {{");
    println!("    let a = vec!{:?};", a);
    println!("    {}", a[1]);
    println!("}}");
}