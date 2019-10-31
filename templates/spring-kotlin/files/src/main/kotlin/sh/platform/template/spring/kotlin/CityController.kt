package sh.platform.template.spring.kotlin

import org.springframework.web.bind.annotation.*

@RestController
class HtmlController(private val repository: CityRepository) {

    @GetMapping("cities")
    fun findAll(): Iterable<City> {
        return repository.findAll()
    }

    @GetMapping("cities/{id}")
    fun getDeveloper(@PathVariable id: Long): City =
            repository.findById(id).orElseThrow { IllegalArgumentException("City does not exist") }

    @DeleteMapping("cities/{id}")
    fun delete(@PathVariable id: Long) {
        repository.deleteById(id)
    }

    @PostMapping("cities")
    fun add(@RequestBody city: City) {
        repository.save(city)
    }
}