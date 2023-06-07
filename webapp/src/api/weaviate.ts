import weaviate, { WeaviateClient } from 'weaviate-ts-client';

const graphqlQuery = 'track_name artist_name track_id album_name duration_ms lyrics album_id';

const client: WeaviateClient = weaviate.client({
  scheme: 'http',
  host: 'localhost:8081',  // Replace with your endpoint
});

// measure time of execution
const measure = async (fn: any) => {
    const start = Date.now();
    const res = await fn();
    const end = Date.now();
    console.log(`Execution time: ${end - start}ms`);

    const duration = end - start;
    return [res, duration];
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

export { getNearText, getAllTracks, measure };
export default client;