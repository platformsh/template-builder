(defsystem example
 :name "example"
 :description "Example of a simple web application on Platform.sh"
 :author "Lisp Coder <user@example.com>"
 :components ((:file "example"))
 :build-operation "asdf:program-op"
 :build-pathname "example"
 :entry-point "example:main"
 :depends-on (:hunchentoot :cl-who))