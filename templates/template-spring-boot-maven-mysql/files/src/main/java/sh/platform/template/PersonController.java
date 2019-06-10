package sh.platform.template;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("people")
public class PersonController {

    @Autowired
    private PersonRepository repository;


    @PostMapping
    @ResponseStatus(code = HttpStatus.CREATED)
    public String save(@RequestBody Person person) {
        repository.save(person);
        return "Saved- " + person.getName();
    }

    @GetMapping(value = "/{id}", produces = "application/json")
    public Person get(@PathVariable("id") long id) {
        return repository.findById(id).orElseThrow(() -> new RuntimeException("Not found"));
    }

    @GetMapping(produces = "application/json")
    public Iterable<Person> get() {
        return repository.findAll();
    }


    @PutMapping(value = "/{id}", produces = "application/json")
    public Person update(@PathVariable("id") long id, @RequestBody Person person) {
        repository.save(person);
        return person;
    }

    @DeleteMapping(value = "/{id}", produces = "application/json")
    public Person delete(@PathVariable("id") long id) {
        Person person = repository.findById(id).orElseThrow(() -> new RuntimeException("Not found"));
        repository.deleteById(id);
        return person;
    }
}
