package sh.platform.template.spring.kotlin

import javax.persistence.Entity
import javax.persistence.GeneratedValue
import javax.persistence.Id

@Entity
data class City(
        var name: String = "",
        var country: String = "",
        @Id @GeneratedValue var id: Long? = null)