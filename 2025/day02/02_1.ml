let to_tuple l =
  match l with
  | x :: y :: _ -> (Stdlib.int_of_string x, Stdlib.int_of_string y)
  | _ -> raise (Failure "Should not happen")

let test_num n =
  let s = Int.to_string n in
  if String.length s mod 2 <> 0 then false
  else
    let l = String.length s in
    let a = String.sub s 0 (l / 2) in
    let b = String.sub s (l / 2) (l / 2) in
    a = b

let rec expand_ranges ab =
  match ab with
  | a, b when a = b -> [ a ]
  | a, b -> a :: expand_ranges (a + 1, b)
;;

In_channel.input_line stdin
|> Option.get |> String.split_on_char ','
|> List.map (String.split_on_char '-')
|> List.map to_tuple |> List.map expand_ranges |> List.flatten
|> List.filter test_num |> List.fold_left ( + ) 0 |> Int.to_string
|> Out_channel.output_string stdout
