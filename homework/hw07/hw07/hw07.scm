(define (filter-lst fn lst)
  (cond 
    ((eq? lst nil) nil)
    ((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
    (else (filter-lst fn (cdr lst)))
  )
)

; ;; Tests
(define (even? x) (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

; similar to question (remove item lst) in lab10
; notice that if the first one is filtered, 
; no need to call (cons (filter-lst fn (cdr lst)) nil), which will cause nested list


(define (interleave first second)
  (cond 
    ((eq? first nil) second)
    ((eq? second nil) first)
    (else (cons (car first) (cons (car second) (interleave (cdr first) (cdr second)))))
  )
)

(interleave (list 1 3 5) (list 2 4 6))
; expect (1 2 3 4 5 6)

(interleave (list 1 3 5) nil)
; expect (1 3 5)

(interleave (list 1 3 5) (list 2 4))
; expect (1 2 3 4 5)


(define (accumulate combiner start n term)
  (cond 
    ((= n 1) (combiner start (term 1)))
    ((> n 0) (combiner (term n) (accumulate combiner start (- n 1) term)))
  )
)


; combiner: a function of two arguments
; start: a number with which to start combining
; n: the number of natural numbers to combine
; term: a function of one argument that computes the nth term of a sequence



(define (no-repeats lst)
  (if (eq? lst nil)
    nil
    (cons (car lst) (no-repeats (filter-lst (lambda (x) (not (= x (car lst)))) (cdr lst))))
  )
)

; attention, I first came up with another procedure showed below
; , which complicated the question and did not totally resolve the question

(define (ff lst)
(begin
(define (f lst num)
  (if (not (eq? (cdr lst) nil))
    (cond
      ((= (car lst) num) (f (cdr lst) num))
      ((not (= (car lst) num)) (cons (car lst) (f (cdr lst) num)))
    )
    lst
  )
)
  (f (cdr lst) (car lst))
))

(begin 
  (define (f lst num)
    (if (not (eq? (cdr lst) nil))
      (cond
        ((= (car lst) num) (f (cdr lst) num))
        ((not (= (car lst) num)) (cons (car lst) (f (cdr lst) num)))
      )
      lst
    )
  )
  (f '(1 3 1 1 5) 1)
)

