let ( >> ) f g = fun x -> g (f x)
let ( << ) f g = fun x -> f (g x)

type dir = Left | Right

let char_to_dir c =
  match c with
  | 'L' -> Left
  | 'R' -> Right
  | _ -> raise (Failure "Should not happen")

let rec read_program c =
  match In_channel.input_line c with
  | None -> []
  | Some s -> s :: read_program c

let rec count_zeros cnt position instrs =
  match instrs with
  | [] -> cnt
  | (Left, x) :: instrs' ->
      update_count cnt ((position - x + 100) mod 100) instrs'
  | (Right, x) :: instrs' ->
      update_count cnt ((position + x + 100) mod 100) instrs'

and update_count cnt position instrs =
  match position with
  | 0 -> count_zeros (cnt + 1) position instrs
  | _ -> count_zeros cnt position instrs
;;

read_program stdin
|> List.map (fun x ->
    ( char_to_dir x.[0],
      String.sub x 1 (String.length x - 1) |> Stdlib.int_of_string ))
|> count_zeros 0 50 |> Int.to_string
|> Out_channel.output_string stdout
