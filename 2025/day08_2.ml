type coord = { x : int; y : int; z : int }

let coord_to_string c =
  String.concat "," (List.map Int.to_string [ c.x; c.y; c.z ])

let ( >> ) f g = fun x -> f x |> g
let trd (_, _, c) = c

let get_coord l =
  match l with
  | x :: y :: z :: _ -> { x; y; z }
  | _ -> raise (Failure "Should not happen")

let distance a b =
  ((a.x - b.x) * (a.x - b.x))
  + ((a.y - b.y) * (a.y - b.y))
  + ((a.z - b.z) * (a.z - b.z))

let rec all_pairs acc l =
  match l with
  | [] -> acc
  | x :: xs ->
      all_pairs
        (List.fold_left (fun acc y -> (x, y, distance x y) :: acc) acc xs)
        xs

let rec root x h =
  match Hashtbl.find h x with x' when x = fst x' -> x' | x' -> root (fst x') h

let union a b h =
  match (root a h, root b h) with
  | (x, _), (y, _) when x = y -> ()
  | (x, sx), (y, sy) when sx < sy ->
      Hashtbl.replace h x (y, sx + sy);
      Hashtbl.replace h y (y, sx + sy)
  | (x, sx), (y, sy) ->
      Hashtbl.replace h x (x, sx + sy);
      Hashtbl.replace h y (x, sx + sy)

let rec union_until_connected h l =
  match l with
  | (a, b) :: l' ->
      union a b h;
      if
        Hashtbl.length h
        = max (Hashtbl.find h a |> snd) (Hashtbl.find h b |> snd)
      then (a, b)
      else union_until_connected h l'
  | _ -> raise (Failure "Should not happen")

let points =
  In_channel.input_all stdin |> String.split_on_char '\n' |> List.rev |> List.tl
  |> List.rev
  |> List.map
       (String.split_on_char ',' >> List.map Stdlib.int_of_string >> get_coord)

let neighbors =
  all_pairs [] points
  |> List.fast_sort (fun a b -> trd a - trd b)
  |> List.map (fun (a, b, _) -> (a, b))

let h = Hashtbl.create (List.length points);;

Hashtbl.add_seq h (List.mapi (fun i x -> (x, (x, 1))) points |> List.to_seq);;

neighbors |> union_until_connected h |> fun (a, b) ->
a.x * b.x |> Int.to_string |> Out_channel.output_string stdout
