import React from "react";
import ReactDOM from "react-dom";
import {
  ApolloClient,
  ApolloProvider,
  HttpLink,
  InMemoryCache,
  split,
} from "@apollo/client";
import { WebSocketLink } from "@apollo/client/link/ws";
import { getMainDefinition } from "@apollo/client/utilities";

import App from "./App";
import { config as platformConfig } from "./utils/platformsh.js";

import "./index.scss";

const config = platformConfig({ envPrefix: "REACT_APP_PLATFORM_" });
const {
  environmentVariables: { NODE_ENV },
  isDev = NODE_ENV === "development",
} = config;

const getApolloUris = () => {
  if (config.hasRelationship("api")) {
    const { host, port } = config.credentials("api");

    if (isDev) {
      return {
        http: `http://${host}:${port}`,
        ws: `ws://${host}:${port}/graphql`,
      };
    }

    const http = Object.entries(config.routes()).find(
      ([, { id }]) => id === "graphqlEntrypoint"
    )[0];
    const wss = Object.entries(config.routes()).find(
      ([, { id }]) => id === "graphqlSubscriptions"
    )[0];

    return {
      http,
      ws: wss.replace("https", "wss"),
    };
  }

  return {
    http: `http://localhost:4000`,
    ws: `ws://localhost:4000/graphql`,
  };
};

const { http, ws } = getApolloUris();

const httpLink = new HttpLink({
  uri: http,
});

const wsLink = new WebSocketLink({
  uri: ws,
  options: {
    reconnect: true,
  },
});

const splitLink = split(
  ({ query }) => {
    const definition = getMainDefinition(query);
    return (
      definition.kind === "OperationDefinition" &&
      definition.operation === "subscription"
    );
  },
  wsLink,
  httpLink
);

const client = new ApolloClient({
  link: splitLink,
  cache: new InMemoryCache(),
});

ReactDOM.render(
  <React.StrictMode>
    <ApolloProvider client={client}>
      <App />
    </ApolloProvider>
  </React.StrictMode>,
  document.getElementById("root")
);
