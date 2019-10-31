package sh.platform.template.spring.kotlin

import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import sh.platform.config.Config
import sh.platform.config.MySQL
import javax.sql.DataSource

@Configuration
class DataSourceConfig {

    @Bean(name = ["dataSource"])
    fun getDataSource(): DataSource {
        val config = Config()
        val database = config.getCredential("database") { MySQL(it) }
        return database.get()
    }
}