package sh.platform.template.spring.kotlin

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration

@SpringBootApplication(scanBasePackages = arrayOf("sh.platform.template.spring.kotlin"),
        exclude = arrayOf(SecurityAutoConfiguration::class))
class Application
    fun main(args: Array<String>) {
        SpringApplication.run(Application::class.java, *args)
    }