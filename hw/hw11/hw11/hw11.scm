(define (find s predicate)
  (if (null? s) #f
    (if (predicate (car s))
    (car s) (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  (cons-stream (* (car s) k)
    (scale-stream (cdr-stream s) K))
)

(define (has-cycle s)
  (if (null? s) #f
    (if (eq? s (cdr-stream s)) #t
     (has-cycle (cdr-stream s))))
)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
