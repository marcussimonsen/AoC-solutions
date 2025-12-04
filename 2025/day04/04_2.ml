let ( >> ) f g = fun x -> g (f x)
let get arr i = try Some (Array.get arr i) with _ -> None
let get_bind arr i = Option.bind arr (fun a -> get a i)
let count_rolls c = match c with Some '@' -> 1 | _ -> 0

let rec find_accessible i j arr =
  match (i, j) with
  | i, _ when i >= Array.length arr -> []
  | _, j when j >= Array.length arr.(i) -> find_accessible (i + 1) 0 arr
  | i, j when arr.(i).(j) <> '@' -> find_accessible i (j + 1) arr
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
      if x < 4 then (i, j) :: find_accessible i (j + 1) arr
      else find_accessible i (j + 1) arr

let rec count_removable acc arr =
  match find_accessible 0 0 arr with
  | [] -> acc
  | l ->
      let _ = List.fold_left (fun _ (i, j) -> arr.(i).(j) <- '.') () l in
      count_removable (acc + List.length l) arr
;;

In_channel.input_all stdin |> String.split_on_char '\n'
|> List.map (String.to_seq >> List.of_seq)
|> List.map Array.of_list |> Array.of_list |> count_removable 0 |> Int.to_string
|> Out_channel.output_string stdout
