let ( >> ) f g = fun x -> g (f x)

let rec transposer i j arr' =
 fun arr ->
  match (i, j) with
  | i, _ when i >= Array.length arr -> arr'
  | _, j when j >= Array.length arr.(i) -> transposer (i + 1) 0 arr' arr
  | i, j ->
      arr'.(j).(i) <- arr.(i).(j);
      transposer i (j + 1) arr' arr

let transpose arr =
  transposer 0 0
    (Array.init
       (Array.length arr.(0))
       (fun _ -> Array.init (Array.length arr) (fun _ -> '.')))
    arr

let op_to_fun op =
  match op with
  | "+" -> ( + )
  | "*" -> ( * )
  | _ -> raise (Failure "Unknown operator")

let op_to_id op =
  match op with "+" -> 0 | "*" -> 1 | _ -> raise (Failure "Unknown operator")

let rec solve_problems acc ops nums =
  match (nums, ops) with
  | [], [] -> raise (Failure "Should not happen")
  | [], op :: _ -> [ List.fold_left (op_to_fun op) (op_to_id op) acc ]
  | "" :: nums', op :: ops' ->
      List.fold_left (op_to_fun op) (op_to_id op) acc
      :: solve_problems [] ops' nums'
  | x :: nums', _ ->
      solve_problems
        ((x |> String.trim |> Stdlib.int_of_string) :: acc)
        ops nums'

let lines =
  In_channel.input_all stdin |> String.split_on_char '\n' |> List.rev |> List.tl

let operations =
  List.hd lines |> String.split_on_char ' ' |> List.filter (fun x -> x <> "")

let nums = List.tl lines |> List.map (String.to_seq >> List.of_seq) |> List.rev
;;

nums |> List.map Array.of_list |> Array.of_list |> transpose |> Array.to_list
|> List.map Array.to_list
|> List.map (List.to_seq >> String.of_seq)
|> List.map String.trim
|> solve_problems [] operations
|> List.fold_left ( + ) 0 |> Int.to_string
|> Out_channel.output_string stdout
