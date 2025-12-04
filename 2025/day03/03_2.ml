(* NOTE: Also solves part 1 *)
(* Just change 12 to 2 *)
let ( >> ) f g = fun x -> g (f x)

let rec read_lines c =
  match In_channel.input_line c with None -> [] | Some l -> l :: read_lines c

let rec find_highest_digit acc l =
  match l with
  | [] -> acc
  | x :: xs when x > acc -> find_highest_digit x xs
  | _ :: xs -> find_highest_digit acc xs

let rec find_x_highest x s =
  match x with
  | 0 -> []
  | _ ->
      let a = String.sub s 0 (String.length s - x + 1)
      |> String.to_seq |> List.of_seq
      |> find_highest_digit '0' in
      let i = String.index s a in
      a :: find_x_highest (x-1) (String.sub s (i+1) (String.length s - i - 1))

let string_to_list = String.to_seq >> List.of_seq
let list_to_string = List.to_seq >> String.of_seq;;

read_lines stdin
|> List.map (find_x_highest 12)
|> List.map list_to_string
|> List.map (Stdlib.int_of_string)
|> List.fold_left (+) 0
|> Int.to_string
|> Out_channel.output_string stdout
