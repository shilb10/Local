(* CS421 - Fall 2014
 * MP1
 *
 * Please keep in mind that there may be more than one
 * way to solve a problem.  You will want to change how a number of these start.
 *)

open Mp1common

(* Problem 1 *)
let random = 17;;  (* You want to change this *)

(* Problem 2 *)
let pi = 3.14159;; (* You want to change this *)

(* Problem 3 *)
let myFirstFun n = 4*(n + 3);;

(* Problem 4 *)
let circumference r = 2.0*.pi*.r;;

(* Problem 5 *)
let double n = (n, 2*n);;

(* Problem 6 *)
let make_bigger x = if x < 0.0 then (-1.0)*.x else if x >= 0.0 && x < 1.0 then x +. 0.5 else x*.x;;

