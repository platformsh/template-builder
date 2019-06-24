package sh.platform.template;

import com.mongodb.MongoClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.mongodb.config.AbstractMongoConfiguration;
import sh.platform.config.Config;
import sh.platform.config.MongoDB;

@Configuration
public class MongoConfig extends AbstractMongoConfiguration {

    private Config config = new Config();

    @Override
    @Bean
    public MongoClient mongoClient() {
        MongoDB mongoDB = config.getCredential("database", MongoDB::new);
        return mongoDB.get();
    }

    @Override
    protected String getDatabaseName() {
        return config.getCredential("database", MongoDB::new).getDatabase();
    }
}