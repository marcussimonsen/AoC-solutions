let rec get_tup l =
  match l with
  | a :: b :: _ -> (a, b)
  | _ -> raise (Failure "Should not happen")

let rec parse_ranges acc l =
  match l with
  | "" :: l' -> acc
  | s :: l' ->
      let chars = String.split_on_char '-' s in
      let t = chars |> List.map Stdlib.int_of_string |> get_tup in
      parse_ranges (t :: acc) l'
  | _ -> raise (Failure "Should not happen")

let rec fix_overlap ranges range =
  match (range, ranges) with
  | _, [] -> [ range ]
  | (a, b), (c, d) :: ranges' when b >= c && b <= d ->
      if a >= c then ranges else (c, d) :: fix_overlap ranges' (a, c - 1)
  | (a, b), (c, d) :: ranges' when a >= c && a <= d ->
      (c, d) :: fix_overlap ranges' (d + 1, b)
  | (a, b), (c, d) :: ranges' when c >= a && c <= b && d >= a && d <= b ->
      fix_overlap ranges' range
  | _, r :: ranges' -> r :: fix_overlap ranges' range
;;

In_channel.input_all stdin |> String.split_on_char '\n' |> parse_ranges []
|> List.fold_left fix_overlap []
|> List.map (fun (a, b) -> b - a + 1)
|> List.fold_left ( + ) 0 |> Int.to_string
|> Out_channel.output_string stdout
