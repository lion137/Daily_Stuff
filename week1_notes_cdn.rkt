#lang racket
(provide (all-defined-out))
;; notes cdn delayed evaluation vid
(define (fact x)
  (if (= x 0)
      1
      (* x (fact (- x 1)))))

(define (if-bad e1 e2 e3)
  (if e1 e2 e3))

;; fact doesnt work with that if-bad

(define (fact-bad x)
  (if-bad (= x 0)
      1
      (* x (fact-bad (- x 1)))))

;;this fact never terminates because if-bad evaluates all three arguments and
;; the last one recur forever

;; but we can delay eval by making zero arg functions from 2 and 3 expresson to bad if:
(define (if-strange-working e1 e2 e3)
  (if e1 (e2) (e3)))

(define (fact-strange x)
  (if-strange-working
   (= x 0)
   (lambda () 1)
   (lambda () (* x (fact-strange (- x 1))))))

; zero arg functionused to delay eval like in this strange-if is called "thunk"

;; lazy evaluation delay and force

(define (my-delay f)
  (mcons #f f))

(define (my-force th)
  (if (mcar th)
      (mcdr th)
      (begin (set-mcar! th #t)
             (set-mcdr! th ((mcdr th)))
             (mcdr th))))
;; when we want to use a thunk we feed to my-force whatever comes from my-delay

(define (power x n)
  (cond
    [(= n 0) 1]
    [(odd? n)  (* x (power (* x x) (/ (- n 1) 2)))]
    [(even? n) (power  (* x x) (/ n 2))]))

(define (power-of-two x)
  (power 2 x))

;;streams
;;recursive thunk gives powers of two asa a pair - first elem is a firt elem
;; it's 2 and therest are in the cdr which is another thunk
(define powers-of-two
  (letrec ([f (lambda (x) (cons x (lambda () (f (* x 2)))))])
    (lambda () (f 2))))
;; tester of the stream:
(define (number-until stream tester)
  (letrec ([f (lambda (stream ans)
                (let ([pr (stream)])
                  (if (tester (car pr))
                      ans
                      (f (cdr pr) (+ ans 1)))))])
    (f stream 1)))
;; stream is a thgunk when called returns a pair with the fitst element as a head
;; of a pair and the rest of elements as stream cdr.

;; stream which produces ones infinitely defined recursively
(define ones (lambda () (cons 1 ones)))

;;stream which defibes the all the natural numbers:

(define (f x) (cons x (lambda () (f (+ x 1)))))
;; defined a function when called returns a pair with x and a thunk wich
;; called returns a pair with x + 1 and a thunk... to mkae a natural number
;; function we need :
(define nats1 (lambda () (f 1)));; we create a stream now

(define nats
  (letrec ([f (lambda (x) (cons x (lambda () (f (+ x 1)))))])
    (lambda () (f 1)))); better way because f is helper fun

;;MEMIZATION

(define (fibo1 x)
  (if ( or (= x 1) (= x 2))
           1
           (+ (fibo1 (- x 1)) (fibo1 (- x 2)))))

;; version with memoization
(define fibonacci
  (letrec([memo null]
          [f (lambda (x)
               (let ([ans (assoc x memo)])
                 (if ans
                     (cdr ans)
                     (let ([new-ans (if (or (= x 1) (= x 2))
                                        1
                                        (+ (f (- x 1))
                                           (f (- x 2))))])
                       (begin
                         (set! memo (cons (cons x new-ans) memo))
                         new-ans)))))])
    f))

