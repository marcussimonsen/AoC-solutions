let ( >> ) f g = fun x -> g (f x)

let rec read_lines c =
  match In_channel.input_line c with None -> [] | Some l -> l :: read_lines c

let rec find_highest_digit acc l =
  match l with
  | [] -> acc
  | x :: xs when x > acc -> find_highest_digit x xs
  | _ :: xs -> find_highest_digit acc xs

let string_to_list = String.to_seq >> List.of_seq
let list_to_string = List.to_seq >> String.of_seq;;

read_lines stdin
|> List.map (fun s ->
    let a =
      find_highest_digit '0'
        (string_to_list (String.sub s 0 (String.length s - 1)))
    in
    let b =
      String.length s - String.index s a - 1
      |> String.sub s (String.index s a + 1)
      |> string_to_list |> find_highest_digit '0'
    in
    [ a; b ] |> list_to_string)
|> List.map (Stdlib.int_of_string)
|> List.fold_left (+) 0
|> Int.to_string
|> Out_channel.output_string stdout
