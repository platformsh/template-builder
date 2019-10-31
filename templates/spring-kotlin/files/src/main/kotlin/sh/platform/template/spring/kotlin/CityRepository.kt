package sh.platform.template.spring.kotlin

import org.springframework.data.repository.CrudRepository

interface CityRepository : CrudRepository<City, Long> {
}