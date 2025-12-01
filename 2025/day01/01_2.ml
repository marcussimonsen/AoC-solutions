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

let rec count_zeros cnt (position : int) instrs =
  match instrs with
  | [] -> cnt
  | (Left, x) :: instrs' -> step cnt position (-x) instrs'
  | (Right, x) :: instrs' -> step cnt position x instrs'

and step cnt position m instrs =
  match m with
  | 0 -> count_zeros cnt position instrs
  | x when x < 0 ->
      if position - 1 = 0 then
        step (cnt + 1) ((position + 99) mod 100) (m + 1) instrs
      else step cnt ((position + 99) mod 100) (m + 1) instrs
  | x ->
      if position + 1 = 100 then
        step (cnt + 1) ((position + 1) mod 100) (m - 1) instrs
      else step cnt ((position + 1) mod 100) (m - 1) instrs
;;

read_program stdin
|> List.map (fun x ->
    ( char_to_dir x.[0],
      String.sub x 1 (String.length x - 1) |> Stdlib.int_of_string ))
|> count_zeros 0 50 |> Int.to_string
|> Out_channel.output_string stdout
