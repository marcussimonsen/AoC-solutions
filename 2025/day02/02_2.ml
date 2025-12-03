#directory "+str";;
#load "str.cma";;

let ( >> ) f g = fun x -> g (f x)

let to_tuple l =
  match l with
  | x :: y :: _ -> (Stdlib.int_of_string x, Stdlib.int_of_string y)
  | _ -> raise (Failure "Should not happen")

let test_num s = Str.string_match (Str.regexp "^\\([0-9]+\\)\\1+$") s 0

let rec expand_ranges ab =
  match ab with
  | a, b when a = b -> [a]
  | a, b -> a :: expand_ranges (a + 1, b)
;;

In_channel.input_line stdin
|> Option.get |> String.split_on_char ','
|> List.map (String.split_on_char '-')
|> List.map to_tuple
|> List.map expand_ranges
|> List.flatten
|> List.filter (Int.to_string >> test_num)
|> List.fold_left ( + ) 0 |> Int.to_string
|> Out_channel.output_string stdout
