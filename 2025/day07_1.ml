let ( >> ) f g = fun x -> f x |> g
let rec find_start i m = match m.(i) with 'S' -> i | _ -> find_start (i + 1) m

let rec shoot i j m =
  if i >= Array.length m then 0
  else
    match m.(i).(j) with
    | 'S' -> shoot (i + 1) j m
    | '|' -> 0
    | '.' ->
        m.(i).(j) <- '|';
        shoot (i + 1) j m
    | '^' -> 1 + shoot i (j - 1) m + shoot i (j + 1) m
    | _ -> raise (Failure "Should not happen")
;;

In_channel.input_all stdin |> String.split_on_char '\n' |> List.rev |> List.tl
|> List.rev
|> List.map (String.to_seq >> Array.of_seq)
|> Array.of_list
|> fun m ->
shoot 0 (find_start 0 m.(0)) m
|> Int.to_string
|> Out_channel.output_string stdout
