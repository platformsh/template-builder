import responseCachePlugin from "apollo-server-plugin-response-cache";

import resolvers from "./resolvers/index.js";
import typeDefs from "./typedefs.js";

import AdditionalEpisodeInfo from "./data-sources/AdditionalEpisodeInfo.js";

export default (db) => ({
  resolvers,
  typeDefs,
  plugins: [responseCachePlugin()],
  dataSources: () => ({
    additionalEpisodeInfo: new AdditionalEpisodeInfo(db.collection("additionalEpisodeInfo"))
  })
});
