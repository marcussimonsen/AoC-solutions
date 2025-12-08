let ( >> ) f g = fun x -> f x |> g
let rec find_start i m = match m.(i) with 'S' -> i | _ -> find_start (i + 1) m

let rec shoot i j m mem =
  if i >= Array.length m then 1
  else
    match m.(i).(j) with
    | 'S' -> shoot (i + 1) j m mem
    | '.' -> shoot (i + 1) j m mem
    | '^' when mem.(i).(j) <> -1 -> mem.(i).(j)
    | '^' ->
        let x = shoot i (j - 1) m mem + shoot i (j + 1) m mem in
        mem.(i).(j) <- x;
        x
    | _ -> raise (Failure "Should not happen")

let m =
  In_channel.input_all stdin |> String.split_on_char '\n' |> List.rev |> List.tl
  |> List.rev
  |> List.map (String.to_seq >> Array.of_seq)
  |> Array.of_list

let memory =
  Array.init (Array.length m) (fun _ ->
      Array.init (Array.length m.(0)) (fun _ -> -1))
;;

shoot 0 (find_start 0 m.(0)) m memory
|> Int.to_string
|> Out_channel.output_string stdout
