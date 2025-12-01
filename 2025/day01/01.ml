let ( >> ) f g = fun x -> g (f x)
let ( << ) f g = fun x -> f (g x)

let rec read_program c =
  match In_channel.input_line c with
  | None -> []
  | Some s -> s :: read_program c

let rec count_zeros cnt position instrs =
  match instrs with
  | [] -> cnt
  | i :: instrs' -> (
      let num = String.sub i 1 (String.length i - 1) |> Stdlib.int_of_string in
      match i.[0] with
      | 'L' -> update_count cnt ((position - num + 100) mod 100) instrs'
      | 'R' -> update_count cnt ((position + num + 100) mod 100) instrs'
      | _ -> raise (Failure "Shouldn't happen"))

and update_count cnt position instrs =
  match position with
  | 0 -> count_zeros (cnt + 1) position instrs
  | _ -> count_zeros cnt position instrs
;;

read_program stdin |> count_zeros 0 50 |> Int.to_string
|> Out_channel.output_string stdout
