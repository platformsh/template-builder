package sh.platform.template.spring.kotlin

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController

@RestController
class HelloController() {

    @GetMapping("/")
    fun helloKotlin(): String {
        return "hello world from Platform.sh"
    }
}