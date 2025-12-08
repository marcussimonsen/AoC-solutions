let rec get_column acc acc' lst =
  match lst with
  | [] -> Some (acc, acc')
  | x :: xs ->
      match x with
      | [] -> None
      | y :: ys -> get_column (y :: acc) (ys :: acc') xs

let rec solve_problems operations nums =
  match operations, get_column [] [] nums with
  | [], _ -> []
  | "*" :: ops, Some (p, nums') ->
    List.fold_left ( * ) 1 p :: solve_problems ops nums'
  | "+" :: ops, Some (p, nums') ->
      List.fold_left (+) 0 p :: solve_problems ops nums'
  | _, _ -> raise (Failure "Should")

let ( >> ) f g = fun x -> g (f x)
let lines = In_channel.input_all stdin |> String.split_on_char '\n' |> List.rev |> List.tl

let operations =
  List.hd lines |> String.split_on_char ' ' |> List.filter (fun x -> x <> "")
let nums =
  List.tl lines
  |> List.map
       (String.split_on_char ' '
       >> List.filter (fun x -> x <> "")
       >> List.map Stdlib.int_of_string);;

solve_problems operations nums
  |> List.fold_left ( + ) 0
  |> Int.to_string
  |> Out_channel.output_string stdout
