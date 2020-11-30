import { pubsub } from "./pubsub.js";

export const Mutation = ({
  upVote(_, { id }, { dataSources: { additionalEpisodeInfo } }) {
    return additionalEpisodeInfo.upVote(id).then((votesUpdated) => {
      pubsub.publish("VOTES_UPDATED", { votesUpdated });
      return typeof votesUpdated !== "undefined";
    });
  },
  downVote(_, { id }, { dataSources: { additionalEpisodeInfo } }) {
    return additionalEpisodeInfo.downVote(id).then((votesUpdated) => {
      pubsub.publish("VOTES_UPDATED", { votesUpdated });
      return typeof votesUpdated !== "undefined";
    });
  },
});
