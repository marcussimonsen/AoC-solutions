let rec get_tup l =
  match l with
  | a :: b :: _ -> (a, b)
  | _ -> raise (Failure "Should not happen")

let rec parse_ranges acc l =
  match l with
  | "" :: l' -> (acc, l')
  | s :: l' ->
      let chars = String.split_on_char '-' s in
      let t = chars |> List.map Stdlib.int_of_string |> get_tup in
      parse_ranges (t :: acc) l'
  | _ -> raise (Failure "Should not happen");;

let rec in_range ingrediant ranges =
  match ranges with
  | [] -> 0
  | (a, b) :: _ when ingrediant >= a && ingrediant <= b -> 1
  | _ :: ranges' -> in_range ingrediant ranges'

let rec in_ranges ingredients ranges =
  match ingredients with
  | [] -> 0
  | ingredient :: ingredients' -> in_range ingredient ranges + in_ranges ingredients' ranges;;

let lines = In_channel.input_all stdin |> String.split_on_char '\n';;

let (ranges, lines) = parse_ranges [] lines;;

let ingredients = lines |> List.filter (fun x -> x <> "") |> List.map Stdlib.int_of_string;;

in_ranges ingredients ranges
|> Int.to_string
|> Out_channel.output_string stdout;;
