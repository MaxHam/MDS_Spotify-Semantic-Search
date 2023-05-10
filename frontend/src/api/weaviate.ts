import weaviate, { WeaviateClient } from 'weaviate-ts-client';

const client: WeaviateClient = weaviate.client({
  scheme: 'http',
  host: 'localhost:8080',  // Replace with your endpoint
});



const getNearText = async(texts: string[], limit=5) => {
    const nearText = {concepts: texts};
    try {
        const res = await client.graphql
            .get()
            .withClassName('Track')
            .withFields('track_name track_artist')
            .withNearText(nearText)
            .withLimit(limit)
            .do();

            console.log(res);
            return res.data.Get.Track;
    } catch (error) {
        console.error(error)
    }
}

const getAllTracks = async(limit=25):Promise<any[]> => {
    try {
        const res = await client.graphql
            .get()
            .withClassName('Track')
            .withFields('track_name track_artist')
            .withLimit(limit)
            .do()

            console.log(res);
            return res.data.Get.Track;
    } catch (error) {
        console.error(error)
    }
    return [];
}

export { getNearText, getAllTracks };
export default client;