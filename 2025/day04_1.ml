let ( >> ) f g = fun x -> g (f x)
let get arr i = try Some (Array.get arr i) with _ -> None
let get_bind arr i = Option.bind arr (fun a -> get a i)
let count_rolls c = match c with Some '@' -> 1 | _ -> 0

let rec count_accessible i j arr =
  match (i, j) with
  | i, _ when i >= Array.length arr -> 0
  | _, j when j >= Array.length arr.(i) -> count_accessible (i + 1) 0 arr
  | _, _ when arr.(i).(j) <> '@' -> count_accessible i (j + 1) arr
  | i, j ->
      let upper_row = get arr (i - 1) in
      let lower_row = get arr (i + 1) in
      let x =
        [
          get_bind upper_row (j - 1);
          get_bind upper_row j;
          get_bind upper_row (j + 1);
          (Some (Array.get arr i) |> fun a -> get_bind a (j - 1));
          (Some (Array.get arr i) |> fun a -> get_bind a (j + 1));
          get_bind lower_row (j - 1);
          get_bind lower_row j;
          get_bind lower_row (j + 1);
        ]
        |> List.map count_rolls |> List.fold_left ( + ) 0
      in
      (if x < 4 then 1 else 0) + count_accessible i (j + 1) arr
;;

In_channel.input_all stdin |> String.split_on_char '\n'
|> List.map (String.to_seq >> List.of_seq)
|> List.map Array.of_list |> Array.of_list |> count_accessible 0 0
|> Int.to_string
|> Out_channel.output_string stdout
