import { pubsub } from "./pubsub.js";

export const Subscription = ({
  votesUpdated: {
    subscribe() {
      return pubsub.asyncIterator(["VOTES_UPDATED"]);
    },
  },
});
