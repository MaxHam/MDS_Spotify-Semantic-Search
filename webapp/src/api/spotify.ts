import axios from "axios";

async function getToken() {
    try {
        const response = await fetch('/auth/token');
        const json = await response.json();
        return json.access_token;
    } catch (error) {
        console.log(error);
    }
  }

const getAlbum = async (id: string, token: string) => {
    try {
        const data = await axios.get(`https://api.spotify.com/v1/albums/${id}`, {
            headers: {
              Authorization: "Bearer " + token,
            },
        }
        );
    
        return data.data;
    } catch (error) {
        console.log(error);
    }
}

export { getAlbum, getToken };