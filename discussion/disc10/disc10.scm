; disc10


; Questions
; scm> (define a (+ 1 2))
; a

; scm> a
; 3

; scm> (define b (- (+ (* 3 3) 2) 1))
; b

; scm> (= (modulo b a) (quotient 5 3))
; #t


;  4.1 What would Scheme display? 
; scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
; 1

; scm> ((if (< 4 3) + -) 4 100)
; -96



; 4. Lambdas and Defining Functions

; Write a function that returns the factorial of a number.
(define (factorial x)
    (cond
        ((= x 1) 1)
        ((<= x 0) 'No factorial)
        ((> x 1) (* x (factorial (- x 1))))
    ) 
)


; Tutorial: Write a function that returns the nth Fibonacci number.
(define (fib n)
    (cond
        ((or (= n 0) (= n 1)) n)
        ((> n 1) (+ (fib (- n 2)) (fib (- n 1))))
    )
)



; 5. Pairs and Lists

; 5.1 Write a function which takes two lists and concatenates them.
; Notice that simply calling (cons a b) would not work because it will create a deep list. 
; Do not call the built-in procedure append, which does the same thing as my-append.
(define (my-append a b)
    (cond
        ((eq? a nil) b)
        ((eq? b nil) a)
        (else (cons (car a) (my-append (cdr a) b)))
    )
)


; 5.2 Tutorial: These short questions are meant to help refresh your memory of topics
; covered in lecture and lab this week before tackling more challenging problems.
; Describe the difference between the following two Scheme expressions. 
; Hint: which defines a new procedure?
; Expression A:
; (define x (+ 1 2 3))
; Expression B:
; (define (x) (+ 1 2 3))
; Expression A means that x = (1 + 2 + 3)
; Expression B defines a new procedure x, which is a lambda expression that takes no argument
; one B is called, the call (1 + 2 + 3) is valued and the result is bound to x

; Write an expression that selects the value 3 from the list below.
; (define s '(5 4 (1 2) 3 7))
; (car (cdr (cdr (cdr s))))



; 5.3 Tutorial: Write a Scheme function that, when given a list, such as (1 2 3 4),
; duplicates every element in the list (i.e. (1 1 2 2 3 3 4 4)).
(define (duplicate lst)
    (cond 
        ((eq? lst nil) nil)
        (else (cons (car lst) (cons (car lst) (duplicate (cdr lst)))))
    )
)

; attention: missing else will cause the second condition of cond inaccessible




; 5.4 Tutorial: Write a Scheme function that, when given an element, a list, and an index, 
; inserts the element into the list at that index.
(define (insert element lst index)
    (cond
        ((and (eq? lst nil) (>= index 0)) (cons element nil))
        ((= index 0) (cons element lst))
        (else (cons (car lst) (insert element (cdr lst) (- index 1))))
    )
)