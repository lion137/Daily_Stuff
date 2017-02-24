#lang racket
;;1

(define (my-range a b c)
  (if (> (+ a c) (+ b c))
      null
      (cons a (my-range (+ a c) b c))))

;; 2

(define (string-append-map xs s)
  (let
      [(st (lambda (x) (string-append x s)))]
  (map st xs)))
