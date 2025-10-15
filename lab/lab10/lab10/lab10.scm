(define (over-or-under num1 num2)
  (cond
      ((< num1 num2) -1)
      ((= num1 num2) 0)
      ((> num1 num2) 1)
  )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0


(define (make-adder num)
  (lambda (inc) (+ num inc))
)

; second question, if write with nested define, it needs to return the nested one
; (define (make-adder num)
;  (define (adder inc)
;   (+ num inc)
; ) adder
; )
; missing adder will cause error

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13


(define (composed f g)
  (define (arg x)
    (f (g x))
  )
  arg
)


(define lst
  (cons (cons 1 nil) (cons 2 (cons (cons 3 (cons 4 nil)) (cons 5 nil))))
)
; writing (cons 1) instead of (cons 1 nil) will cause error: incorrect number of arguments: #[cons]


(define (remove item lst)
    (if (eq? lst nil)
        nil
    (if (= (car lst) item)
        (remove item (cdr lst))
        (cons (car lst) (remove item (cdr lst))))))

; original idea, cause error because (cons (remove item (cdr lst)) nil) leads to nested list
; (if (= (car lst) item)
;               (cons (remove item (cdr lst)) nil)
;               (cons (car lst) (remove item (cdr lst)))
;        )

; other's solution on the Internet
;  (cond
;    ((eq? lst nil) nil)
;    ((= (car lst) item) (remove item (cdr lst)))
;    (else (cons (car lst) (remove item (cdr lst))))
;  )

; writing (nil) instead of nil causes error: nil is not callable: ()


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

