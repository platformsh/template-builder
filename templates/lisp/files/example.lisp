(defpackage #:example
  (:use :hunchentoot :cl-who :cl)
  (:export main)

(in-package #:example)

(defvar *acceptor* (make-instance 'easy-acceptor :port (uiop:getenv "PORT")))

(define-easy-handler (greet :uri "/hello") (name)
  (with-html-output-to-string (s) (htm (:body (:h1 "hello, " (str name))))))

(export 'main)
(defun main ()
  (start *acceptor*)
  (sleep most-positive-fixnum))