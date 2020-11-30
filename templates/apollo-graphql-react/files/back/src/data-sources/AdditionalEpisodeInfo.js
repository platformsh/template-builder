import { MongoDataSource } from "apollo-datasource-mongodb";

export default class AdditionalEpisodeInfo extends MongoDataSource {
  getAdditionalEpisodeInfo(id) {
    return this.findOneById(id);
  }

  getUpVotes(id) {
    return this.getAdditionalEpisodeInfo(id).then(
      ({ upVotes } = {}) => upVotes
    );
  }

  getDownVotes(id) {
    return this.getAdditionalEpisodeInfo(id).then(
      ({ downVotes } = {}) => downVotes
    );
  }

  upVote(id) {
    return this.collection
      .findOneAndUpdate(
        { _id: id },
        { $set: { _id: id }, $inc: { upVotes: 1 } },
        { upsert: true, returnOriginal: false }
      )
      .then(({ value, ok }) => (ok === 1 ? value : {}));
  }

  downVote(id) {
    return this.collection
      .findOneAndUpdate(
        { _id: id },
        { $set: { _id: id }, $inc: { downVotes: 1 } },
        { upsert: true, returnOriginal: false }
      )
      .then(({ value, ok }) => (ok === 1 ? value : {}));
  }
}
