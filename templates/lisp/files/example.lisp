(defpackage "hello-world" (:use :hunchentoot :cl-who :cl))
(in-package "hello-world")
(defvar *acceptor* (make-instance 'easy-acceptor :port (uiop:getenv "PORT")))

(define-easy-handler (greet :uri "/hello") (name)
  (with-html-output-to-string (s) (htm (:body (:h1 "hello, " (str name))))))

(start *acceptor*)