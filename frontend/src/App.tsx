import { useEffect, useState } from 'react'
import './App.css'
import { getAllTracks, getNearText } from './api/weaviate'

function App() {
  const [tracks, setTracks] = useState<any[]>([])
  const [searchTerm, setSearchTerm] = useState<string>("")
  useEffect(() => {
    getAllTracks().then((newTracks) => setTracks(newTracks));
  }, [])

  const handleChange = async(event: any) => {
    console.log(event.target.value);
    setSearchTerm(event.target.value);
  }

  const handleSubmit = async(event: any) => {
    event.preventDefault();
    if(searchTerm=== "" || !searchTerm) {
      return;
    }
    const filteredTracks = await getNearText([searchTerm]);
    console.log(filteredTracks);
    setTracks(filteredTracks);
  }

  return (
    <>
      <h1>Spotify Semantic Search</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Search for a track:
          <input type="text" value={searchTerm} onChange={handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
      <div className="card">
        <ul>
          {tracks.map((track) => (
            <li key={track.track_id}>{track.track_name} - {track.track_artist}</li>
          ))}
        </ul>
      </div>
    </>
  )
}

export default App
