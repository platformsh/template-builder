import { ApolloServer } from "apollo-server";
import MongoClient from "mongodb";
import { config as platformConfig } from "platformsh-config";

import getApolloConfig from "./apollo-config.js";

const config = platformConfig();

const credentials = config.credentials("database");
const client = await MongoClient.connect(
  config.formattedCredentials("database", "mongodb"),
  { useUnifiedTopology: true }
);
const db = client.db(credentials.path);

const server = new ApolloServer(getApolloConfig(db));

server
  .listen({
    port: config.port,
  })
  .then(({ url, subscriptionsUrl }) => {
    console.log(`Server ready at ${url}`);
    console.log(`Subscriptions ready at ${subscriptionsUrl}`);
  });
