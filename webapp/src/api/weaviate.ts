import weaviate, { WeaviateClient } from 'weaviate-ts-client';

const graphqlQuery = 'track_name artist_name track_id album_name duration_ms lyrics album_id';

const client: WeaviateClient = weaviate.client({
  scheme: 'http',
  host: 'localhost:8080',  // Replace with your endpoint
});


const ask = async(question: string, limit=16) => {
    const withAsk = {
        question,
        // properties: ['summary'],
    };

    try {
        const res = await client.graphql
            .get()
            .withClassName('Track')
            .withAsk(withAsk)
            .withFields(`${graphqlQuery} _additional { answer { hasAnswer certainty property result startPosition endPosition } }`)
            .withLimit(limit)
            .do()
            return res.data.Get.Track;
    } catch (error) {
        console.error(error)
    }
}

const getNearText = async(texts: string[], limit=16) => {
    const nearText = {concepts: texts};
    try {
        const res = await client.graphql
            .get()
            .withClassName('Track')
            .withFields(graphqlQuery)
            .withNearText(nearText)
            .withLimit(limit)
            .do();

            return res.data.Get.Track;
    } catch (error) {
        console.error(error)
    }
}

const getAllTracks = async(limit=16):Promise<any[]> => {
    try {
        const res = await client.graphql
            .get()
            .withClassName('Track')
            .withFields(graphqlQuery)
            .withLimit(limit)
            .do()
            return res.data.Get.Track;
    } catch (error) {
        console.error(error)
    }
    return [];
}

export { getNearText, getAllTracks, ask };
export default client;