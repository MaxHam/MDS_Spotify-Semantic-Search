// import weaviate, { WeaviateClient } from 'weaviate-ts-client';

// const client: WeaviateClient = weaviate.client({
//   scheme: 'http',
//   host: 'localhost:8080',  // Replace with your endpoint
// });

// const classObj = {
//     'class': 'Lyrics',
//     'vectorizer': 'text2vec-transformers'  // Or 'text2vec-cohere' or 'text2vec-huggingface'
//   }
  
// // add the schema
// client
//   .schema
//   .classCreator()
//   .withClass(classObj)
//   .do()
//   .then((res: any) => {
//     console.log(res)
//   })
//   .catch((err: Error) => {
//     console.error(err)
//   });



// async function importQuestions() {
// // Get the data from the data.json file
// const data = await getJsonData();

// // Prepare a batcher
// let batcher = client.batch.objectsBatcher();
// let counter: number = 0;
// let batchSize: number = 100;

// interface Question {
//     Answer: string;
//     Question: string;
//     Category: string;
// }

// data.forEach((question: Question) => {
//     // Construct an object with a class and properties 'answer' and 'question'
//     const obj = {
//     class: 'Question',
//     properties: {
//         answer: question.Answer,
//         question: question.Question,
//         category: question.Category,
//     },
//     }

//     // add the object to the batch queue
//     batcher = batcher.withObject(obj);

//     // When the batch counter reaches batchSize, push the objects to Weaviate
//     if (counter++ == batchSize) {
//     // flush the batch queue
//     batcher
//     .do()
//     .then((res: any) => {
//         console.log(res)
//     })
//     .catch((err: Error) => {
//         console.error(err)
//     });

//     // restart the batch queue
//     counter = 0;
//     batcher = client.batch.objectsBatcher();
//     }
// });

// // Flush the remaining objects
// batcher
// .do()
// .then((res: any) => {
//     console.log(res)
// })
// .catch((err: Error) => {
//     console.error(err)
// });
// }

// importQuestions();


// export default client;